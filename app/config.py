import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables ASAP

debug = True if os.getenv("DEBUG") == "1" else False

bot_username = os.getenv("BOT_USERNAME")
bot_token = os.getenv("BOT_TOKEN")

# Database configuration
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "dev_forge_bot")
db_user = os.getenv("DB_USER", "postgres")
db_pass = os.getenv("DB_PASS", "postgres")
db_port = os.getenv("DB_PORT", "5432")

db_url = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
