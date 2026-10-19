import os
from dotenv import load_dotenv

# .env file se variables load karega
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Admin ID (Owner ke liye)
OWNER_ID = 8630156174 # Apna Telegram ID yahan dalein
