from datetime import datetime
from typing import List
from urllib import response
from xmlrpc.client import Boolean
import flask
import requests
from flask import Flask, Response, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from typing import List
from app.model import Question, db

app: flask.app.Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'
db.init_app(app)

@app.route("/", methods=["POST"])
def handler():
    request_data = request.get_json()
    question_amount: int = request_data["questions_num"] 
    questions: List[Question] = request_questions(question_amount)
    
    lastq: Question = get_previous_question()
    write_batch_questions(questions)
    
    return Response (
        jsonify(lastq)
    )

def request_questions(amount: int) -> List[Question]:
    request_datetime: datetime = datetime.now
    result: List[Question] = []
    
    r = requests.get("https://jservice.io/api/random?count=%(amount)d"%{"amount": amount})
    questions: dict = r.json
    for i in questions:
        q: Question = Question(i, request_datetime)
        result.append(make_unique(q))
    return result

def make_unique(q: Question, dt: datetime) -> Question:
    if Question.query.filter_by(id=q.id).first() != None :
        r = requests.get("https://jservice.io/api/random?count=1")
        qq = Question(r.json[0], dt)
        return make_unique(qq, dt)
    else:
        return q

def get_previous_question() -> Question:
    q = Question.query.order_by("requested_at").first()
    return q

def write_batch_questions(questions: List[Question]):
    for q in questions:
        db.session.add(q)
    db.session.commit()

if __name__ == "__main__":
    db.create_all()
    app.run(debug=False)