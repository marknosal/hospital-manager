import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_direct_path = os.path.dirname(os.path.abspath(__file__))

DATABASE_URI = f'sqlite:///{os.path.join(db_direct_path, "phase3_database.db")}'

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
