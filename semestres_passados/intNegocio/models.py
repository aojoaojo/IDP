from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import *
import uuid
from datetime import datetime

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

def generate_now():
    return datetime.now().strftime("%d-%m-%y %H:%M:%S")

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    created = Column(String, default=generate_now)
    email = Column(String, unique=True)

    relationship("Task")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=generate_uuid)
    created = Column(String, default=generate_now)
    updated = Column(DateTime, nullable=True)
    task = Column(String, nullable=False)
    status = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=False)

    user_id = Column(String, ForeignKey("users.id"))
