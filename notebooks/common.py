import ast
import json
import logging
import re
from functools import wraps

import pandas as pd
from snowflake.ml.registry import Registry
from snowflake.snowpark import Session
from snowflake.snowpark import functions as F
from snowflake.snowpark import types as T


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Running {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Finished {func.__name__} with result: {result}")
        except Exception as e:
            logging.error(f"Error occurred in {func.__name__}: {e}")
            raise
        else:
            return result

    return wrapper


def convert_to_all_caps(c):
    """
    Converts a given string to all capital letters and separates words with underscores.

    Args:
        c (str): The input string to be converted.

    Returns:
        str: The converted string with all capital letters and underscores separating words.
    """
    return re.sub(
        r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])",
        "_",
        c,
    ).upper()


def rename_columns_all_caps(df):
    """
    Renames all columns in the DataFrame to uppercase.

    Args:
        df (snowpark.DataFrame): The input DataFrame.

    Returns:
        snowpark.DataFrame: The DataFrame with all column names converted to uppercase.
    """
    return df.to_df([convert_to_all_caps(c) for c in df.columns])


def read_url_csv(session: Session, url: str):
    df_pandas = pd.read_csv(url)
    df = rename_columns_all_caps(session.create_dataframe(df_pandas))
    return df


def get_col_types(df, type):
    """
    Returns a list of column names in a DataFrame that match the specified data type.

    Args:
        df: The DataFrame to search for column types.
        type (str): The data type to filter columns by. Valid values are "string" and "numeric".

    Returns:
        list: A list of column names that match the specified data type.

    Raises:
        ValueError: If the specified type is not "string" or "numeric".
    """
    if type == "string":
        return [c.name for c in df.schema if isinstance(c.datatype, (T.StringType))]
    elif type == "numeric":
        return [
            c.name
            for c in df.schema
            if isinstance(
                c.datatype, (T.DoubleType, T.IntegerType, T.LongType, T.FloatType)
            )
        ]
    else:
        raise ValueError(f"Invalid type: {type}")


def get_next_version(reg, model_name) -> str:
    """
    Returns the next version of a model based on the existing versions in the registry.

    Args:
        reg: The registry object that provides access to the models.
        model_name: The name of the model.

    Returns:
        str: The next version of the model in the format "V_<version_number>".

    Raises:
        ValueError: If the version list for the model is empty or if the version format is invalid.
    """
    models = reg.show_models()
    if models.empty:
        return "V_1"
    elif model_name not in models["name"].to_list():
        return "V_1"
    max_version_number = max(
        [
            int(version.split("_")[-1])
            for version in ast.literal_eval(
                models.loc[models["name"] == model_name, "versions"].values[0]
            )
        ]
    )
    return f"V_{max_version_number + 1}"


def count_all_nulls(df) -> dict:
    """
    Counts the number of null values in each column of a DataFrame and returns a dictionary
    with column names as keys and the corresponding count of null values as values.

    Args:
        df: The DataFrame to count null values in.

    Returns:
        dict: A dictionary with column names as keys and the count of null values as values.
    """
    return {
        k: v
        for k, v in {
            c: df.where(F.col(c).is_null()).count() for c in df.columns
        }.items()
        if v > 0
    }


def get_version_with_highest_accuracy(reg: Registry, model_name: str):
    """
    Returns the version name of the model with the highest accuracy.

    Parameters:
    reg (Registry): The Registry object.
    model_name (str): The name of the model.

    Returns:
    str: The version name of the model with the highest accuracy.
    """
    model_versions = reg.get_model(model_name).show_versions()
    model_versions["accuracy"] = model_versions["metadata"].apply(
        lambda x: json.loads(x).get("metrics", {}).get("Accuracy", None)
    )
    return (
        model_versions.sort_values(by="accuracy", ascending=False)
        .head(1)["name"]
        .values[0]
    )


def get_infer_schema(reg: Registry) -> T.StructType:
    m = reg.get_model("TITANIC")
    mv = m.default

    input_schema = T.StructType(
        [
            T.StructField(input.name, input.as_snowpark_type())
            for input in [
                fx.get("signature").inputs
                for fx in mv.show_functions()
                if fx.get("name") == "PREDICT"
            ][0]
        ]
    )
    return input_schema
