from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_models.models import User,Task

# Create a connection to the database
e = create_engine('postgresql://postgres:123@localhost:5432/postgres', echo=True)

# Create a session
session = sessionmaker(bind=e)

# Create a new user
def add_user(name, email):
    with session() as s:
        user = User(name=name, email=email)
        s.add(user)
        s.commit()
        return user.id

def insert_task(task, status, priority, deadline, user_id, updated=None):
    with session() as s:
        task = Task(task=task, status=status, priority=priority, deadline=deadline, user_id=user_id)
        s.add(task)
        s.commit()
    
def get_user(user_id):
    with session() as s:
        return s.query(User).filter_by(id=user_id).first()
