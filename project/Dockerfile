# pull official base image
FROM python:3.8

# set working directory
WORKDIR /usr/src/app

# Linux Updates
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install nano

# install python dependencies
RUN python -m pip install --upgrade pip
RUN pip install Cython
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .
