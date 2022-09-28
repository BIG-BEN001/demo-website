# Base Image
FROM python:3.10.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV PIP_ROOT_USER_ACTION=ignore

RUN adduser -D myuser
USER myuser

# Working Directory
WORKDIR /website


RUN python -m venv denv
# Installing Dependencies
COPY requirements.txt /website/
# RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m pip install --upgrade pip && pip install virtualenv && virtualenv install --system

# Copy project files and directories
COPY . /website/