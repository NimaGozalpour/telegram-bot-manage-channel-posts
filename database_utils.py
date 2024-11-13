from sqlalchemy import orm
import models
from schemas import *


def add_admin(user: User, db: orm.Session):

    new_user = models.BotUsers(user_id = user.user_id,
                               password = user.password,
                               can_add_admin = user.can_add_admin,
                               creation_date = user.creation_date)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def user_exist(user_id: int, db: orm.Session):
    exist = db.query(models.BotUsers).filter(models.BotUsers.user_id == user_id).first() is not None

    return exist

