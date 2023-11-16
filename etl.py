""" Python Extraction """


# Import python packages
import requests 
import pandas as pd 
from sqlalchemy import create_engine
import yaml

# Extract

def extract()-> dict:
    # This API extracts data from http://universities.hipolabs.com
    API_URL = "http://universities.hipolabs.com/search?country=United+States"

    # Send a GET request to the API and convert the response to JSON format
    data = requests.get(API_URL).json()

    # Return data           
    return data

# Transform

def transform(data: dict) -> pd.DataFrame:
    # Create a DataFrame from the input data
    df = pd.DataFrame(data)

    # Print the total number of universities from API
    print(f"Total number of universities from API {len(data)}")

    # Filter the DataFrame to include only universities in Texas
    df = df[df["name"].str.contains("Texas")]

    # Print the number of universities after filtering for those in Texas
    print(f"Number of universities in Texas {len(df)}")

    # Convert lists in the 'domains' and 'web_pages' columns to strings
    df['domains'] = [','.join(map(str, l)) for l in df['domains']]
    df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]

    # Reset the index of the DataFrame
    df = df.reset_index(drop=True)

    # Return a subset of the DataFrame with selected columns
    return df[["domains", "country", "web_pages", "name"]]


def load(df: pd.DataFrame) -> None:

    # Open the 'config.yaml' file in read mode ('r')
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)['mysql']

    # Start MYSql Connection
    mysql_credentials = f"mysql+mysqlconnector://{config['username']}:{config['password']}@{config['host']}/{config['database']}"

    # Connect SQLAlchemy to connect MYSql
    mysql_engine = create_engine(mysql_credentials)

    # Table name
    table_name = 'texas_universities'

data = extract()
df = transform(data)