# 🎂 Birthday Automation Bot 🤖

## Overview

The **Birthday Automation Bot** is a scheduled Python script designed to automatically check a source file for birthdays every morning and generate a personalized WhatsApp message for the project owner to manually forward. This tool ensures no important project member's birthday is missed.

The script runs continuously on a server (like Codespaces) and is scheduled to execute its main logic at a specific time each day (e.g., 9:00 AM).

## ✨ Features

  * **Scheduled Daily Check:** The bot runs silently and checks for birthdays daily using the Python `schedule` library.
  * **Data Source Flexibility:** Reads birthday data, names, and custom quotes from a simple CSV file.
  * **Personalized Messaging:** Generates a unique, personalized birthday message using the person's name and a custom quote from the data source.
  * **Project Owner Notification:** Instead of sending messages directly to recipients (which requires complex, paid API integration), the bot generates a **clickable WhatsApp URL** directed only to the **Project Owner's number** for easy, manual forwarding.

-----

## ⚙️ Setup and Installation

### Prerequisites

1.  **Python 3.x**
2.  **Git** (for version control and cloning)
3.  **A Stable Server Environment** (e.g., Codespaces, a persistent server, or a local machine that remains running).

### 1\. Clone the Repository

```bash
git clone <your-repository-url>
cd birthday-bot
```

### 2\. Install Dependencies

Install the required Python libraries (`pandas` for data handling and `schedule` for automation):

```bash
pip install pandas schedule
```

### 3\. Data Preparation (`birthdays.csv`)

Ensure you have a CSV file named **`birthdays.csv`** in the root directory with the following structure. **Note:** The bot looks for the exact headers below:

| Name | Month | Day | Quote |
| :--- | :--- | :--- | :--- |
| Jane Doe | 10 | 12 | Go get 'em\! |
| John Smith | 1 | 25 | Keep fighting the good fight. |

-----

## 🛠️ Configuration

All necessary configuration is handled within the **`main.py`** file.

### 1\. Set the Project Owner's Phone Number

The bot needs to know where to send the final notification link. Update the `PROJECT_OWNER_PHONE` constant in `main.py`:

```python
# main.py
PROJECT_OWNER_PHONE = "+15555555555" # <-- REPLACE WITH YOUR ACTUAL NUMBER (e.g., +11234567890)
```

### 2\. Set the Scheduled Time

The script is currently scheduled to run every day at 9:00 AM. You can change this in `main.py`:

```python
# main.py (around line 52)
# Change the time to your desired daily check time
schedule.every().day.at("09:00").do(run_birthday_bot)
```

-----

## ▶️ Running the Bot

To initiate the continuous scheduler, run the script from your terminal:

```bash
python main.py
```

### Expected Output:

The script will begin running and remain active.

```
Bot is running and checking for birthdays every day at 09:00...
Press Ctrl+C to stop the scheduler.
```

If a birthday is found on the scheduled check, the output will look like this:

```
--- Phase 1: Data Loading ---

--- Phase 2: Birthday Checking ---
🎉 SUCCESS: Found 1 birthday(s) today!

--- Phase 3 & 4: Message Generation & Sending ---
All messages will be directed to the Project Owner's number: +15555555555

--- FINAL STEP: MANUAL MESSAGE SEND ---
🔗 URL generated for phone number: +15555555555
Please copy the URL below, paste it into your browser, and click 'Send' on WhatsApp Web.

🔗 WhatsApp URL: https://web.whatsapp.com/send?phone=15555555555&text=...[encoded-message-here]
```

**ACTION REQUIRED:** Copy the URL and paste it into a web browser where you are logged into WhatsApp Web to manually forward the message.

-----

## 📁 Project Structure

The project is broken down into modular files for easy maintenance:

```
.
├── src/
│   ├── data_loader.py         # Loads and validates data from birthdays.csv.
│   ├── birthday_checker.py    # Filters the data to find today's birthdays.
│   ├── message_generator.py   # Formats the personalized birthday message text.
│   └── whatsapp_sender.py     # Generates the final, clickable WhatsApp URL.
├── main.py                    # The central coordinator, configuration, and scheduler.
├── birthdays.csv              # The data source (required).
└── README.md                  # This file.
```
