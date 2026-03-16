"""
Save Restricted Content Bot Configuration

Developed by: Anuj kumar
Telegram: @anujedits76 X @Anujkumar_21

Please retain this credit if you use or modify this project.
"""

import os


# ==============================
# Telegram Bot Credentials
# ==============================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8770843324:AAHkflqRUjhBvcul6EnNljZfJ6d9FSzj204")
API_ID = int(os.environ.get("API_ID", "34446649"))
API_HASH = os.environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")


# ==============================
# Admin Configuration
# ==============================

# Fetch ADMINS from environment variables, default to one admin if not set
ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "7892805795").split(",") if admin]


# ==============================
# Database Configuration
# ==============================

DB_URI = os.environ.get("DB_URI", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Anujedit")


# ==============================
# Logging Configuration
# ==============================

# Replace with your Telegram log channel ID (example: -1001234567890)
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003515041061"))


# ==============================
# Error Handling
# ==============================

# Set to True to send error messages to users
ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"
