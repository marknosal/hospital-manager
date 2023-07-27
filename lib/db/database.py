from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///phase3_database.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
