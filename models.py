from sqlalchemy import Column, Integer, Float, String, Boolean
from database import Base


# Create the models (tables)
class product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    productId = Column(String)
    modelNumber = Column(String)
    price = Column(String)
    salePrice = Column(String)
    #discount = Column(String)
    title = Column(String)
    subTitle = Column(String)
    rating = Column(String)
    ratingCount = Column(String)
    brand = Column(String)
    sale = Column(String)
    gender = Column(String)
    outlet = Column(String)
    color = Column(String)
    sku = Column(String)
    availability = Column(String)
    size = Column(String)

