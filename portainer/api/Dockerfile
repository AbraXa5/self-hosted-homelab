# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

WORKDIR /app
COPY ./app /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=portainer_api.py
CMD ["sh", "-c", "flask run --host=0.0.0.0"]
