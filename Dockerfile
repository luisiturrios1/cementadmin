FROM python:2.7.16

ENV PYTHONUNBUFFERED 1
ENV SERVER_HOST 0.0.0.0
ENV SERVER_PORT 8080

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN ["pip", "install", "--no-cache-dir", "-r", "requirements.txt"]

COPY ./ /usr/src/app

ENTRYPOINT ["/bin/bash", "/usr/src/app/entrypoint.sh"]
