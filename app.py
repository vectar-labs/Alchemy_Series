import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


# Adding data into the database  / Create : C

"""
user_3 = User(name="Cyril Ramaphosa", age = 64)
user_4 = User(name="Baraka Mpanzu", age = 58)
user_5 = User(name="Willow Mic", age = 24)

# session.add(user) - This add a single data entry

session.add_all([user_3, user_4, user_5])
session.commit()
"""

# Quering data from database / Read  : R

"""

users = session.query(User).all()

for user in users:
    print(f'User id:{user.id}, name: {user.name}, age: {user.age}')

"""
    

# filtering data to select data we want

"""
user = session.query(User).filter_by(id=1).one_or_none()

# incase you are looking for multile similar data
user = session.query(User).filter_by(id=1).all()
user = session.query(User).filter_by(id=1).first()
print(user.name)

"""

# Update the data  / U

"""
user = session.query(User).filter_by(id=1).one_or_none()

# update the name 

user.name = 'Different name'
session.commit()

print(user.name)


"""

# Delete data / D

"""
user = session.query(User).filter_by(id=1).one_or_none();

session.delete(user)

session.commit()

"""

"""
names = ['Anderw Pip', 'Iron Man','John Doe', 'Jane Doe']
ages = [23, 45, 67, 31, 90,44]


for x in range(6):
    user = User(name = random.choice(names), age = random.choice(ages))
    session.add(user)

session.commit()

"""

# Ordering all users ordered by age (ascending )

"""
users = session.query(User).order_by(User.age).all()

for user in users:
    print(f'User id:{user.id}, name: {user.name}, age: {user.age}')



"""

# Ordering all users ordered by age (Descending )

# users = session.query(User).order_by(User.age.desc()).all()
"""
users = session.query(User).order_by(User.age, User.name).all()

for user in users:
    print(f'User id:{user.id}, name: {user.name}, age: {user.age}')
"""


#  Query all users with age greater than or equal to 35

# users_all = session.query(User).all()

# users_filtered = session.query(User).filter(User.age >= 35, User.name =='Jane Doe').all()
# users_filtered = session.query(User).filter_by(age=45).all() This does not work with condtions like >= or <=
# print('All users:',  len(users_all))
# print('Filtered users', len(users_filtered))

# users = session.query(User).where(User.age>=45, User.name=='Iron Man').all() # This is equivalent to using AND operator
# users = session.query(User).where(and_(User.age>=45, User.name=='Iron Man')).all() # This is equivalent to using AND operator
# users = session.query(User).where((User.age>=45) & (User.name=='Iron Man')).all() # This is equivalent to using AND operator


# users = session.query(User).where(or_(User.age>=45, User.name=='Iron Man')).all() # This is equivalent to using OR operator
users = session.query(User).where((User.age>=45) | (User.name=='Iron Man')).all() # This is equivalent to using OR operator

for user in users:
    print(f'User id:{user.id}, name: {user.name}, age: {user.age}')



