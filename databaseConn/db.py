from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session  # Added for type hinting if needed

DATABASE_URL = ""  
# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session maker that will generate new Session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()
