from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime
from database import Base


# Create the models (tables)
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    productId = Column(String)
    productName = Column(String)
    brand = Column(String)
    productType = Column(String)
    subType = Column(String)
    price = Column(Float)
    salePrice = Column(Float)
    description = Column(String)
    rating = Column(String)
    ratingCount = Column(String)
    sale = Column(String)
    availability = Column(String)
    creation_date = Column(DateTime)
    last_modified = Column(DateTime)


# Create the models (tables)
class BotUsers(Base):
    __tablename__ = 'bot_user'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    can_add_admin = Column(Boolean)
    creation_date = Column(DateTime)
    signed_in = Column(DateTime)




