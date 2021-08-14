FROM python:3.9.6-slim-buster

RUN mkdir /wjproject
WORKDIR /wjproject

COPY requirements.txt /wjproject/
RUN pip install -r requirements.txt

COPY . /wjproject
CMD python manage.py runserver 0.0.0.0:8000





