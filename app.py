import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_, not_, func
from models import User,Address, engine

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
# users = session.query(User).where((User.age>=45) | (User.name=='Iron Man')).all() # This is equivalent to using OR operator

# for user in users:
#     print(f'User id:{user.id}, name: {user.name}, age: {user.age}')

#  Using NOT operator

# users = session.query(User).where(not_(User.name=='Jane Doe')).all()
# for user in users:
#     print(f'User id:{user.id}, name: {user.name}, age: {user.age}')


"""
users = (
    session.query(User).where(
        and_(
        not_(User.name == "Jane Doe"),
        and_(User.age > 35, 
             User.age < 60
    )
        )
                              )
).all()

for user in users:
    print(f'User id:{user.id}, name: {user.name}, age: {user.age}')


"""

# Python SQLAlchemy ORM - Grouping and Chaining

# group users by age using func - function from sqlalchemy

# users = session.query(User.age, func.count(User.id)).group_by(User.age).all()

"""
users = session.query(User.name, func.count(User.id)).group_by(User.name).all()

name_count = 0
common_name =""
for name, value in users:
    
    if value > name_count:
        name_count = value
        common_name = name
    
    if value == 1:
        print(f"There is {value} person called {name}")
    else:
        print(f"There are {value} people are called {name}")

print(f" The common name is {common_name}")



"""

# Chaining

"""

users = session.query(User).filter(User.age > 37).filter(User.age < 80).all()
for user in users:
    print(f'User id:{user.id}, name: {user.name}, age: {user.age}')

"""
    
#  chaining multiple queries

"""
users_tuple = (
    session.query(User.age, func.count(User.id))
    .filter(User.age > 40)
    .order_by(User.age)
    .filter(User.age < 70)
    .group_by(User.age)
    .all()
)


for age, count in users_tuple:
    print(f" Age: {age} - {count} users")
    


"""
    
# Using conditionals

# only_iron_man = True

"""
only_iron_man = False
group_by_age = True

users = session.query(User)

if only_iron_man:
    users = users.filter(User.name == "Iron Man")

if group_by_age:
    
    users.group_by(User.age)

users = users.all()

for user in users:
    print(f"User age:{user.age}, name: {user.name}")


"""



# data_set = [["", 0] for _ in range(10)]

# for index in range(10):
#     name = input("Enter a name: ")
#     age = int(input('Enter age: '))
#     data_set[index][0] = name
#     data_set[index][1] = age
        


# print(data_set)



#################################################

# Python SQLAlchemy ORM - 1 to MANY Relationships

################################################

# create users from models file

user_1 = User(name='John Moremi', age=28)
user_2 = User(name='Mwiza Charles', age=26)
user_3 = User(name='Magoso Lameck', age=30)

# Create Addresses

# address_1 = Address(city='Dar es Salaam', country='Tanzania', zip_code='+255')
# address_2 = Address(city='Dodoma', country='Tanzania', zip_code='+200')
# address_3 = Address(city='Tabora', country='Tanzania', zip_code='+120')

# associate addresses with users

# user_1.addresses.extend([address_1, address_2])
# user_2.addresses.append(address_3)

# Adding users and address to the session and committing changes to the database

# Create following relationship

user_1.following.append(user_2)
user_2.following.append(user_1)
user_3.following.append(user_2)

session.add_all([user_1, user_2, user_3])
session.commit()

print(f"{user_1.following =}")

# users = session.query(User).all();

# for user in users:
#     cities = [address.city for address in user.addresses]
#     print(f"name: {user.name}, lives in {', '.join(cities)}")

