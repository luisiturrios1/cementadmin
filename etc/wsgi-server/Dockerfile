FROM python:2.7.16

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN ["pip", "install", "--no-cache-dir", "-r", "requirements.txt"]

COPY ./src /usr/src/app

EXPOSE 3031

CMD ["uwsgi", "--module", "cementadmin.wsgi:application", "--master", "--processes", "1", "--die-on-term", "--socket", "wsgi-server:3031"]