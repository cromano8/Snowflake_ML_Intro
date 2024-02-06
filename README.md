# Snowflake for Data Science

[![Test Dependencies](https://github.com/cromano8/Snowflake_ML_Intro/actions/workflows/notebooks.yml/badge.svg)](https://github.com/cromano8/Snowflake_ML_Intro/actions/workflows/notebooks.yml)

### Getting Started

- 🎥 **Intro Video Walkthrough:** [Snowflake for ML Intro](https://github.com/cromano8/Snowflake_ML_Intro/assets/59093254/c249ce4c-2494-49ba-8142-6aec21cc4b08)
- 🎥 **End-to-End ML Ops in Snowflake:** [Live: End-to-End ML Ops in Snowflake](https://www.youtube.com/watch?v=prA014tFRwY)
- 🔗 **Regular 30-Day Trial:** [Sign Up](https://signup.snowflake.com/)
- 🔗 **Student/Educator 120-Day Trial:** [Sign Up (Student)](https://signup.snowflake.com/?trial=student)

Although we recorded videos, we are constantly making upgrades and additions to this repo, so the videos may differ slightly from what is in the repo.  Overall they are the same but we will continue to upload more videos on any additions to the repo.

## Configuration Setup

1. Create a `.env` file and populate it with your account details:

    ```plaintext
    SNOWFLAKE_ACCOUNT = abc123.us-east-1
    SNOWFLAKE_USER = username
    SNOWFLAKE_PASSWORD = yourpassword
    SNOWFLAKE_ROLE = sysadmin
    SNOWFLAKE_WAREHOUSE = compute_wh
    SNOWFLAKE_DATABASE = snowpark
    SNOWFLAKE_SCHEMA = titanic
    ```

2. Utilize the `environment.yml` file to set up your Python environment for the demo:
    - Examples in the terminal:
        - `conda env create -f environment.yml`
        - `micromamba create -f environment.yml -y`

Why we partner with Anaconda

<img src="https://github.com/cromano8/Snowflake_ML_Intro/assets/59093254/8ebc0c29-e1fd-459f-b564-535e970b0732" alt="Image" width="80%" height="80%">

Review of distributed Hyperparameter tuning benefits

Local run time 8 min 27 seconds <br>

![Screenshot 2024-02-05 at 10 13 50 AM](https://github.com/cromano8/Snowflake_ML_Intro/assets/59093254/7721cbc8-3fff-4fb4-9767-c3aadf1ac239)

SnowflakeML run time 1 min 17 seconds (6.5x improvement in speed leveraging a Large WH)

![Screenshot 2024-02-05 at 10 16 43 AM](https://github.com/cromano8/Snowflake_ML_Intro/assets/59093254/6b30e9b0-a47e-4558-aa98-05d71cf01802)

## Data Processing & ML Operations

### Load & Transform Data

Execute the `load_data` notebook to accomplish the following:

- Load the Titanic dataset from Seaborn, convert to uppercase, and save as CSV
- Upload the CSV file to a Snowflake Internal Stage
- Create a Snowpark DataFrame from the staged CSV
- Write the Snowpark DataFrame to Snowflake as a table

### Machine Learning Operations (snowml)

In the `snowml` notebook:

- Generate a Snowpark DataFrame from the Titanic table
- Validate and handle null values
- Remove columns with high null counts and correlations
- Adjust Fare datatype and impute categorical nulls
- One-Hot Encode Categorical Values
- Segregate data into Test & Train sets
- Train an XGBOOST Classifier Model with hyperparameter tuning
- Conduct predictions on the test set
- Display Accuracy, Precision, and Recall metrics

### Advanced MLOps with Live/Batch Inference & Streamlit

Following the `load_data` steps, utilize the deployment notebook to:

- Create a Snowpark DataFrame from the Titanic table
- Assess and eliminate columns with high null counts and correlated columns
- Adjust Fare datatype and handle categorical nulls
- One-Hot Encode Categorical Values
- Split the data into Test & Train sets
- Train an XGBOOST Classifier Model, optimizing with grid search
- Display model accuracy and best parameters
- Register the model in the model registry
- Deploy the model as a vectorized UDF (User Defined Function)
- Execute batch predictions on a table
- Perform real-time predictions using Streamlit for interactive inference
