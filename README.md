# Introduction to using Snowflake for datascience

## Create a .env file and include the following filling in your account URL/Username/Password

```
SNOWFLAKE_ACCOUNT = abc123.us-east-1
SNOWFLAKE_USER = username
SNOWFLAKE_PASSWORD = yourpassword
SNOWFLAKE_ROLE = sysadmin
SNOWFLAKE_WAREHOUSE = compute_wh
SNOWFLAKE_DATABASE = snowpark
SNOWFLAKE_SCHEMA = titanic
```

## Use the environment.yml file to create a Python environment for the demo
Examples in the terminal
- `conda env create -f environment.yml`
- `micromamba create -f environment.yml -y`


## Run the load_data notebook which will perform the following tasks
- Load Titanic dataset from Seaborn, uppercase the column names and convert to csv
- Put the CSV file into a Snowflake Internal Stage
- Create a Snowpark DataFrame from the CSV in the stage
- Write the Snowpark DataFrame to Snowflake as a table <br>

## Run the snowml notebook which will perform the following tasks
- Create a Snowpark DataFrame from the Titanic table
- Check Null values
- drop columns with high count of nulls
- Convert Fare datatype
- Impute Categorical columns with nulls
- One Hot Encode Categrocial Values
- Split into Test & Train
- Train an XGBOOST Classifier Model
- Perform predictions on test
- Return Accuracy, Precision, and Recall

# End to End MLOps with live/batch inference and Streamlit
### After running load_data instead of running the snowml notebook, this one uses the deployment notebook
- Create a Snowpark DataFrame from the Titanic table
- Check Null values
- drop columns with high count of nulls, and correlated columns
- Convert Fare datatype
- Impute Categorical columns with nulls
- One Hot Encode Categrocial Values
- Split into Test & Train
- Train an XGBOOST Classifier Model with gridsearch and hyperparameters
- Return Accuracy and best parameters
