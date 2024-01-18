from sqlalchemy import create_engine  #The function from SQLAlchemy is used to create a database engine
from sqlalchemy.ext.declarative import declarative_base #
from sqlalchemy.orm import sessionmaker #Created using the sessionmaker function from SQLAlchemy's orm module.It configures the session to be used for database operations.

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:nandini@localhost/nandini'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()