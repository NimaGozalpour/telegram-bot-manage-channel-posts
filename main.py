from dotenv import load_dotenv
import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.apihelper import ApiTelegramException
from sqlalchemy import orm
from database import engine, get_db
from database_utils import add_admin, user_exist
import models
from datetime import datetime
from schemas import *
import hashing
#from 


#create all tables
models.Base.metadata.create_all(engine)

# Load environment variables from the .env file
load_dotenv()

# Access API key securely from environment
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)


def check_bot_api_key_connection():
    check_flag = False
    try:
        bot_info = bot.get_me()
        print("API key is valid.")
        print("Bot Info:", bot_info)
        check_flag = True
    except ApiTelegramException as e:
        print("API key is invalid. Error:", e)

    return check_flag


def intializion_config_file():

    check_bot_api_key_connection()
 
    super_user = {'user_id': os.getenv("ADMIN_USER"),
                  'password': hashing.hash(os.getenv('ADMIN_PASSWORD')),
                  'can_add_admin': True,
                  'creation_date': datetime.now(),
                  }

    user = User(**super_user)
    with next(get_db()) as session_db:
        if not user_exist(user.user_id, session_db):
            add_admin(user, session_db)
        else:
            print(session_db.query(models.BotUsers).filter(models.BotUsers.user_id == user.user_id).all())
            pass

intializion_config_file()    


@bot.message_handler(commands=['start'])
def start_bot(message):
    user_info = message.from_user
    
    # Extract specific information
    user_id = user_info.id
    username = user_info.username
    first_name = user_info.first_name
    last_name = user_info.last_name if user_info.last_name else ""
    
    # Log or store the information (print here for demonstration)
    print(f"User ID: {user_id}")
    print(f"Username: {username}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")

    # Create a keyboard button to request phone number
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    phone_button = KeyboardButton(text="شماره تلفن خود را ارسال کنید", request_contact=True)
    markup.add(phone_button)

    # Send a welcome message in Persian
    bot.send_message(message.chat.id, f"سلام {first_name}! لطفاً برای استفاده از این ربات، شماره تلفن خود را ارسال کنید.", reply_markup=markup)

# Handle the contact response with the phone number
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.contact is not None:
        phone_number = message.contact.phone_number
        user_info = message.from_user

        user_id = user_info.id
        
        print(f"Received phone number: {phone_number} {user_id}")  # Debug: print to console
        bot.reply_to(message, f"از اینکه شماره تلفن خود را به اشتراک گذاشتید متشکرم: {phone_number}")

        #check if user_id and phone_number have access to bot
        with next(get_db()) as session_db:
            check_flag = hashing.check_user_pass(user_id, phone_number, session_db)

        if check_flag:
            bot.reply_to(message, f"ورود شما با موفقیت انجام شد.")
        
        else:
            bot.reply_to(message, f"ورود شما نا موفقیت بود.")

    else:
        print("No contact information received.")  # Debug: for cases where contact is None





bot.polling()
