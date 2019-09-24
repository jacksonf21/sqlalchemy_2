from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://test:123@localhost:5432/film')
Session = sessionmaker(bind=engine)

Base = declarative_base()


