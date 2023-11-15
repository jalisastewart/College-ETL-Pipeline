""" Python Extraction """


# Import python packages

import requests
import pandas as pd
from sqlalchemy import create_engine

# Extract

def extract()-> dict:
    # This API extracts data from http://universities.hipolabs.com
    API_URL = "http://universities.hipolabs.com/search?country=United+States"

    # Send a GET request to the API and convert the response to JSON format
    data = requests.get(API_URL).json()

    # Return data           
    return data