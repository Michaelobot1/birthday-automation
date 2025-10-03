# src/whatsapp_sender.py
import urllib.parse

def send_whatsapp_message(phone_number, message):
    """
    Generates a clickable WhatsApp Web URL for the project owner to manually 
    send the message, bypassing Codespace browser restrictions.

    Args:
        phone_number (str): The single Project Owner's phone number (e.g., +11234567890).
        message (str): The personalized birthday message to be sent.
    """
    
    # Clean the phone number (remove leading '+') if necessary, 
    # but the API usually handles the '+' well. We'll ensure it starts with the country code.
    cleaned_number = phone_number.lstrip('+')

    # The message must be URL-encoded to handle spaces, commas, and special characters correctly.
    encoded_message = urllib.parse.quote(message)

    # Construct the official WhatsApp Web URL format
    whatsapp_url = (
        f"https://web.whatsapp.com/send?phone={cleaned_number}"
        f"&text={encoded_message}"
    )

    # Print the URL for the owner to manually click and send
    print("\n--- FINAL STEP: MANUAL MESSAGE SEND ---")
    print(f"🔗 URL generated for phone number: {phone_number}")
    print("Please copy the URL below, paste it into your browser, and click 'Send' on WhatsApp Web.")
    print(f"\n🔗 WhatsApp URL: {whatsapp_url}\n")
