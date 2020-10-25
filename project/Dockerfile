# pull official base image
FROM python:3.8-slim-buster

# install linux updates
RUN apt-get update
RUN apt-get upgrade -y
#RUN apt-get install g++ -y

# install python dependencies
RUN python -m pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# set working directory
WORKDIR /usr/src/project

# add app
COPY . .
