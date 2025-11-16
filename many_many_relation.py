from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine, Table, DateTime)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime


db_url = "sqlite:///app_database.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


##################  STUDENT TO COURSE MANY TO MANY RELATIONSHIP   #############

"""

# Create relationship between students and courses

# Association table

# student_course_link = Table('student_course', Base.metadata,
#                             Column('student_id', Integer, ForeignKey('students.id')),
#                             Column('course_id', Integer, ForeignKey('courses.id'))
                            # )
                            
class StudentCourse(Base):
    __tablename__ ='student_course'
    id = Column(Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    course_id = Column('course_id', Integer, ForeignKey('courses.id'))
    

class Student(Base):
    __tablename__ ='students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # courses = relationship('Course', secondary=student_course_link)
    courses = relationship('Course', secondary='student_course', back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    # students = relationship('Student', secondary=student_course_link)
    students = relationship('Student', secondary='student_course', back_populates='courses')

"""




##################  PATIENTS TO DOCTOR  APPOINTMENT MANY TO MANY RELATIONSHIP   #############

"""

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey('patients.id'))
    appointment_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)
    
    doctor = relationship('Doctor', backref='appointments') # - this define the tendancy of doctor to have multiple appointments
    patient = relationship('Patient', backref='appointments')

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    specialty = Column(String)


class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(DateTime)
    

"""
####  USER FOLLOWERS AND FOLLOWING MANY TO MANY RELATIONSHIP

class UserAssociation(Base):
    __tablename__ = 'user_associations'
    id = Column(Integer, primary_key=True)
    
    follower_id = Column(Integer, ForeignKey('users.id'))
    following_id = Column(Integer, ForeignKey('users.id'))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    following = relationship(
        'User',
        secondary='user_asspciations',
        primaryjoin='UserAssociation.follower_id==User.id',
        secondaryjoin='UserAssociation.following_id==User.id',
        backref='followers'
    )
    
    
    def _repr__(self):
        return f"<User:{self.name}>"
    


Base.metadata.create_all(engine)
    
# Add data into database
# computer = Course(title='Computer Science')
# chemistry = Course(title='Chemistry')
# bill = Student(name='Bill', courses = [computer, chemistry])
# bob = Student(name='Bob', courses = [computer, chemistry])


# session.add_all([computer, chemistry, bill, bob])
# session.commit()

# bob_courses = session.query(Student).filter_by(name='Bob').first()
# courses = [course.title for course in bob_courses.courses]
# print(f"Bob's courses: {','.join(courses)}")
# bill_courses = session.query(Student).filter_by(name='Bill').first()
# courses = [course.title for course in bill_courses.courses]
# print(f"Bill's courses: {','.join(courses)}")


# APPOINTMENTS SCENARIO

# dr_abdulaziz = Doctor(name='Abdulaziz', specialty='Cardiology')
# john_doe = Patient(name="John Doe", dob=datetime(1990,1,1))
# appointment = Appointment(doctor=dr_abdulaziz, patient=john_doe, notes='Routine check-up')

# session.add_all([dr_abdulaziz, john_doe, appointment])
# session.commit()

# Find all appointments for Dr, Abdulaziz

# appointments_for_dr_abdulaziz = session.query(Doctor).filter(Appointment.doctor.has(name='Abdulaziz')).all()

# print("Dr. Abdulaziz's Appointments")
# print(appointments_for_dr_abdulaziz)

# # Find all appointments for John Doe the patient

# appointments_for_john_done = session.query(Doctor).filter(Appointment.patient.has(name='John Doe')).all()

# print("John Doe's Appointments")
# print(appointments_for_john_done)