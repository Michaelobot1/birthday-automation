
from src.data_loader import load_birthday_data

def run_check():
    birthday_data = load_birthday_data() # Ask the loader to get the data

    if birthday_data is not None:
        print("--- Data Loader Test Successful! ---")
        print("Your data looks like this:")
        print(birthday_data.head()) # Shows the first few rows
    else:
        print("Test Failed. Check your data file.")

if __name__ == '__main__':
    run_check()