FROM python:latest

WORKDIR /app
COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false 
RUN poetry install