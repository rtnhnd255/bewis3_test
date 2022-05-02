from crypt import methods
from urllib import response
import requests
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''

@app.route("/", methods=["POST"])
def handler():
    question_number: int = request.args.get("questions_num", type=int) 
    r = requests.get("https://jservice.io/api/random?count=1")
    return Response (
        r.text,
        content_type=r.headers["content-type"]
    )

if __name__ == "__main__":
    app.run(debug=False)