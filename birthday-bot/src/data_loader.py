

import pandas as pd
import os
from pathlib import Path

def load_birthday_data():
    """Reads the CSV file, converts the date column, and returns the data."""
    
    # 1. Use the 'pathlib' module to find the ABSOLUTE path to the project root.
    # This makes the code immune to where you run it from in the terminal.
    # It starts from the location of this script (data_loader.py) and goes up two levels (.. / ..)
    # The first '..' goes to 'src', the second '..' goes to the project root.
    project_root = Path(__file__).parent.parent.resolve()
    
    # 2. Build the full path to the CSV file
    # This combines the root path with the 'data' folder and the filename.
    file_path = project_root / 'data' / 'birthdays.csv'

    try:
        # Check if the file exists before attempting to read it
        if not file_path.exists():
            print(f"ERROR: Data file not found. Checked path: {file_path}")
            return None
        
        # 3. Read the CSV file into a DataFrame
        df = pd.read_csv(file_path, usecols=['Name', 'Birthday', 'Quote'])

        # 4. Convert the 'Birthday' column to Date Objects. (Assuming MM/DD/YYYY)
        df['Birthday'] = pd.to_datetime(df['Birthday'], format='%m/%d/%Y')
        
        return df

    except Exception as e:
        print(f"An error occurred during data loading: {e}")
        return None

    
