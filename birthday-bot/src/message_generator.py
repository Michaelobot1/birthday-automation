# src/message_generator.py
import datetime

# FIX IS HERE: The function uses 'name' and 'quote' directly, matching the definition.
def generate_message(name, quote): 
    """
    Generates a personalized birthday message using an F-string.

    Args:
        name (str): The name of the person celebrating.
        quote (str): The personalized quote for the message.

    Returns:
        str: The full, formatted birthday message.
    """
    
    # 1. Get the current year for a slight personalization touch
    current_year = datetime.datetime.now().year

    # 2. Use an F-string to construct the message
    # 'name' and 'quote' are used directly here, avoiding the NameError.
    message = (
        f"🎉 Happy Birthday, {name}! 🎉\n\n"
        f"Wishing you a year filled with success and happiness, courtesy of your Project Bot.\n\n"
        f"A thought for your day (from your data sheet):\n"
        f'"{quote}"\n\n'
        f"Sent on {current_year}"
    )

    return message
