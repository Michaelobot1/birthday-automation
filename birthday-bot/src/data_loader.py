
# TODO: Import the pandas library and give it the standard short name, 'pd'.
import pandas as pd
import os
# create function to read data from csv file
def load_birthday_data():
    # Directions to find the file: Go up (..), into 'data/', find the file.
    file_path = '../data/birthdays.csv'
    try:
        df = pd.read_csv(file_path, usecols=['Name', 'Birthday', 'Quote'])
        df['Birthday'] = pd.to_datetime(df['Birthday'], format='%m/%d/%Y')

        return df # Hand the clean spreadsheet data back
    except FileNotFoundError:
        print(f"ERROR: Data file not found. Check path: {file_path}")
        return None


    
