from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


db_url = "sqlite:///app_database.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()

# Define models and create One to One relationship

class User(Base):
    __tablename__ ='users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship('Address', back_populates='user', uselist=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='address')
    
    

Base.metadata.create_all(engine)


# create new user and address

# new_user = User(name="Micky Mouse")
# new_address = Address(email="micky@mic.com", user=new_user)

# add data to the database

# session.add(new_user)
# session.add(new_address)

# session.commit()

user = session.query(User).filter_by(name='Micky Mouse').first()

print(f"Name: {user.name}, address = {user.address.email}")



