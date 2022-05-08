FROM python:3.10

RUN apt-get update
RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV = "docker"
EXPOSE 5000