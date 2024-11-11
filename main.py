from dotenv import load_dotenv
import os


# Load environment variables from the .env file
load_dotenv()

# Access API key securely from environment
api_key = os.getenv("TELEGRAM_API_KEY")