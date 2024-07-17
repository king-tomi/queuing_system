from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_data_model_visualizer import generate_data_model_diagram

# Define SQLAlchemy models for your tables (replace with your actual data types)
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    CustomerID = Column(Integer, primary_key=True)
    Name = Column(String)
    ContactDetails = Column(String)
    ServiceType = Column(String)

    queue_entries = relationship("Queue", backref="customer")
    feedbacks = relationship("Feedback", backref="customer")


class Queue(Base):
    __tablename__ = "queues"

    QueueID = Column(Integer, primary_key=True)
    CustomerID = Column(Integer, ForeignKey("customers.CustomerID"))
    Status = Column(String)
    Timestamp = Column(String)


class Staff(Base):
    __tablename__ = "staff"

    StaffID = Column(Integer, primary_key=True)
    Name = Column(String)
    Role = Column(String)
    ContactDetails = Column(String)

    feedbacks = relationship("Feedback", backref="staff")


class Feedback(Base):
    __tablename__ = "feedback"

    FeedbackID = Column(Integer, primary_key=True)
    CustomerID = Column(Integer, ForeignKey("customers.CustomerID"))
    StaffID = Column(Integer, ForeignKey("staff.StaffID"), nullable=True)
    FeedbackText = Column(String)
    Rating = Column(Integer)
    Timestamp = Column(String)

# Generate the ERD image (replace "erd.png" with your desired filename and format)
generate_data_model_diagram([Customer, Queue, Staff, Feedback], "erd.svg")
add_web_font_and_interactivity('erd.svg', 'erd_interactive.svg')


print("ERD generated successfully! Check the file: erd.png")