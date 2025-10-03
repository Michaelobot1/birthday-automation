 

import pandas as pd
from datetime import date # We only need the 'date' class from the datetime module

def get_today_birthdays(df):
    """
    Accepts the full DataFrame and returns a smaller DataFrame containing 
    only the classmates with a birthday today.

    Args:
        df (pd.DataFrame): The processed DataFrame containing Name, Birthday (Date Object), and Quote.

    Returns:
        pd.DataFrame: A DataFrame containing only the rows where the birthday matches today's month and day.
    """
    
    # 1. Get Today's Date and Components
    today = date.today()
    today_month = today.month
    today_day = today.day

    # 2. Extract DataFrame Components
    # We use the special '.dt' accessor on the Date Object column to pull out 
    # the month and day number from the stored birthdays.
    df['B_Month'] = df['Birthday'].dt.month
    df['B_Day'] = df['Birthday'].dt.day

    # 3. The Match/Filter (Boolean Indexing)
    # This is the core logic: 
    #   - We create a condition where the DataFrame's Month equals Today's Month (Condition 1)
    #   - AND (using the & symbol) where the DataFrame's Day equals Today's Day (Condition 2)
    # The result is a new DataFrame containing only the matching rows.
    df_birthdays = df[ 
        (df['B_Month'] == today_month) & 
        (df['B_Day'] == today_day) 
    ]
    
    # 4. Clean up the temporary columns before returning
    df_birthdays = df_birthdays.drop(columns=['B_Month', 'B_Day'])
    
    return df_birthdays
