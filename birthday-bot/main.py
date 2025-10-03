# main.py
# The central entry point that coordinates all modules:
# Data Loader -> Birthday Checker -> Message Generator -> WhatsApp Sender

# The single number that will receive all the generated messages for manual forwarding.
PROJECT_OWNER_PHONE = "+2348113077882" # <-- REPLACE WITH YOUR ACTUAL NUMBER (e.g., +11234567890)

from src.data_loader import load_birthday_data
from src.birthday_checker import get_today_birthdays
from src.message_generator import generate_message
from src.whatsapp_sender import send_whatsapp_message

def run_birthday_bot():
    """
    Main function to run the entire birthday automation pipeline.
    """
    # 1. DATA LOADING
    print("\n--- Phase 1: Data Loading ---")
    birthday_data = load_birthday_data()

    if birthday_data is None:
        print("🛑 Critical Failure: Cannot proceed without data.")
        return

    # 2. BIRTHDAY CHECKING
    print("\n--- Phase 2: Birthday Checking ---")
    birthdays_today = get_today_birthdays(birthday_data)

    if birthdays_today.empty:
        print("💤 No birthdays found today. Shutting down until tomorrow.")
        return

    print(f"🎉 SUCCESS: Found {len(birthdays_today)} birthday(s) today!")
    
    # 3. MESSAGE GENERATION AND SENDING
    print("\n--- Phase 3 & 4: Message Generation & Sending ---")
    print(f"All messages will be directed to the Project Owner's number: {PROJECT_OWNER_PHONE}")
    
    # Iterate through every person found with a birthday today
    for index, person in birthdays_today.iterrows():
        name = person['Name']
        quote = person['Quote']
        
        # CRITICAL FIX: We no longer try to read 'Phone' from the person, 
        # avoiding the 'KeyError'.

        # Generate the personalized message
        final_message = generate_message(name, quote)
        print(f"\n✅ Message generated for {name}.")
        
        # Call the sender function, always using the single owner's number
        # This will print a clickable URL for the owner to send the message.
        send_whatsapp_message(PROJECT_OWNER_PHONE, final_message)


if __name__ == '__main__':
    run_birthday_bot()
