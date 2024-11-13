from dataclasses import dataclass
import bcrypt
from passlib.context import CryptContext
import models
from sqlalchemy import orm


@dataclass
class SolveBugBcryptWarning:
    __version__: str = getattr(bcrypt, "__version__")


setattr(bcrypt, "__about__", SolveBugBcryptWarning())

pwd_context = CryptContext(schemes=['bcrypt'], deprecated = "auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def check_user_pass(user_id: int, phone_number: int, db: orm.Session):
    user = db.query(models.BotUsers).filter(models.BotUsers.user_id == user_id).first()
    check_flag = False
    if not user:
        print('user id is not found')

    elif not verify(phone_number, user.password):
        print('user password is wrong')
    
    else:
        print('Ready to go')
        check_flag = True

    return check_flag
