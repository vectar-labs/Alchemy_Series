from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

#  "dialect+driver://username:password@host:port/database name"

# db_url = "postgresql+psycopg2://postgres:kitindi@localhost:5432/alchemy_db"
db_url = "sqlite:///databse.db"
engine = create_engine(db_url)


Base = declarative_base() # used for creating database models

# creating tables / models
# Python SQLAlchemy ORM - 1 to MANY Relationships

    
# Unmapped Mathod

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    
    id = Column(Integer, primary_key=True)

class Address(BaseModel):
    __tablename__ = 'addresses'
    
    city = Column(String)
    country = Column(String)
    zip_code = Column(String)
    user_id = Column(ForeignKey('users.id'))
    user = relationship('User', back_populates='addresses')
    
    def __repr__(self):
        return f"<Address(id={self.id}, city='{self.city}')>"
class FollowingAssociation(BaseModel):
    __tablename__ ='following_association'
    user_id = Column(Integer, ForeignKey('users.id'))
    following_id = Column(Integer, ForeignKey('users.id'))
    
    

class User(Base):
    __tablename__ ='users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses = relationship('Address')
    # setting up user following 
    ##### version 1 ####
    # following_id = Column(Integer, ForeignKey('user.id'))
    # following = relationship('User', remote_side=[id], uselist=True)
    
    #### Version 2 Best way ####
    following = relationship(
        'User',
        secondary='following_association',
        primaryjoin='FollowingAssociation.user_id == User.id',
        secondaryjoin='FollowingAssociation.following_id == User.id'
    )
    
    def __repr__(self):
        return f"<Address(id={self.id}, name='{self.name}')>"
    
    
    
    
    
    
    
Base.metadata.create_all(engine)