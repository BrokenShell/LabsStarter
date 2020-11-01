# pulls official base image
FROM python:3.8-slim-buster

# sets unbuffered python IO
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# installs linux updates
RUN apt-get update
RUN apt-get upgrade -y

# sets working directory & adds files
WORKDIR /usr/src/project
COPY project .

# installs dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#ENTRYPOINT uvicorn --app app.main:API --host=0.0.0.0 --port=8000
#EXPOSE 8000/tcp

# docker build . -t hrf-ds-api
# docker run -p 8000:8000 hrf-ds-api
