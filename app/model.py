from datetime import date
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Question(Base):
    __tablename__ = "questions"

    id: int = Column(Integer, primary_key=True)
    question: str = Column(String)
    answer: str = Column(String)
    timestamp: date = Column(Date)

