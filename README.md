# Snowflake for Data Science

### Getting Started

🎥 **Intro Video Walkthrough:** [Snowflake for ML Intro](https://github.com/cromano8/Snowflake_ML_Intro/assets/59093254/c249ce4c-2494-49ba-8142-6aec21cc4b08)  
🎥 **Advanced MLops Video Walkthrough:** [Snowflake for MLOps](https://github.com/cromano8/Snowflake_ML_Intro/assets/59093254/38c0eede-eb23-4971-99d8-425c7f9bfa4d)  
🔗 **Regular 30-Day Trial:** [Sign Up](https://signup.snowflake.com/)  
🔗 **Student/Educator 120-Day Trial:** [Sign Up (Student)](https://signup.snowflake.com/?trial=student)  

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
