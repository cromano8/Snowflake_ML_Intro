# Introduction to using Snowflake for datascience <br>
### Video Walkthrough <br>
https://github.com/cromano8/Snowflake_ML_Intro/assets/59093254/c249ce4c-2494-49ba-8142-6aec21cc4b08 <br>

Student/Educator 120 day trial - https://signup.snowflake.com/?trial=student<br>

Regular 30 day trial - https://signup.snowflake.com/<br>

## Create a .env file and include the following filling in your account URL/Username/Password<br>

SNOWFLAKE_ACCOUNT = abc123.us-east-1<br>
SNOWFLAKE_USER = username<br>
SNOWFLAKE_PASSWORD = yourpassword<br>
SNOWFLAKE_ROLE = sysadmin<br>
SNOWFLAKE_WAREHOUSE = compute_wh<br>
SNOWFLAKE_DATABASE = snowpark<br>
SNOWFLAKE_SCHEMA = titanic<br>

## Use the environment.yml file to create a python environment for the demo <br>
Examples in the terminal <br>
- conda env create -f environment.yml <br>
- micromamba create -n from_file -f environment.yml -c conda-forge <br>


## Run the load_data notebook which will perform the following tasks <br>
- Load Titanic dataset from Seaborn, uppercase the column names and convert to csv
- Put the CSV file into a Snowflake Internal Stage
- Create a Snowpark DataFrame from the CSV in the stage
- Write the Snowpark DataFrame to Snowflake as a table <br>

## Run the snowml notebook which will perform the following tasks <br>
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
