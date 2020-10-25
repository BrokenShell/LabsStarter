# pulls official base image
FROM python:3.8-slim-buster

# sets unbuffered python IO
ENV PYTHONUNBUFFERED=1

# installs linux updates
RUN apt-get update
RUN apt-get upgrade -y

# sets working directory & adds files
WORKDIR /usr/src/project
COPY . .

# installs dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
