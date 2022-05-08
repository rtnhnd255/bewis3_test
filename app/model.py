from datetime import datetime
from logging.config import dictConfig
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()
db = SQLAlchemy()
class Question(Base):
    __tablename__ = "questions"

    id: int = db.Column(db.Integer, primary_key=True)
    question: str = db.Column(db.String())
    answer: str = db.Column(db.String())
    timestamp: datetime = db.Column(db.DateTime)

    def __init__(self, i: dict):
        self.id = i['id']
        self.question = i['question']
        self.answer = i['answer']
        ss = i['created_at'].replace('T', " ").split(".")[0]
        self.timestamp = datetime.strptime(ss, "%Y-%d-%m %H:%M:%S")
