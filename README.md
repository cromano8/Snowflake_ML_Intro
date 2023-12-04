# Introduction to using Snowflake for datascience
### Video Walkthrough
https://github.com/cromano8/Snowflake_ML_Intro/assets/59093254/c249ce4c-2494-49ba-8142-6aec21cc4b08

Sign up for a regular trial at https://signup.snowflake.com/ or if you're a student or an educator, 
you can use the 120-day trial at https://signup.snowflake.com/?trial=student.

## Create a file named ".env".
Replace these values with your credentials.
```
SNOWFLAKE_ACCOUNT = abc123.us-east-1
SNOWFLAKE_USER = username
SNOWFLAKE_PASSWORD = yourpassword
SNOWFLAKE_ROLE = sysadmin
SNOWFLAKE_WAREHOUSE = compute_wh
SNOWFLAKE_DATABASE = snowpark
SNOWFLAKE_SCHEMA = titanic
```

## Create a Python environment for the demo
Using the terminal, execute one of the following commands, depending on your package manager. 

**conda**
```bash
conda env create -f environment.yml
```
**micromamba**
```bash
micromamba create --file environment.yml
```

## Run the load_data notebook which will perform the following tasks
- Load the Titanic dataset from Seaborn, uppercase the column names and convert to csv
- Put the CSV file into a Snowflake Internal Stage
- Create a Snowpark DataFrame from the CSV in the stage
- Write the Snowpark DataFrame to Snowflake as a table <br>

## Run the snowml notebook, which will perform the following tasks
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
