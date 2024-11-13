from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# Define the engine and session
DATABASE_URL = "sqlite:///SGfruit.db"

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base model
Base = declarative_base()

# Function to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


