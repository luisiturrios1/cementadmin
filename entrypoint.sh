#!/bin/bash

run-migrations() {
    echo "Try running django migrations: python manage.py migrate"
    python manage.py migrate
}

uwsgi-server() {
    echo "Running server: uwsgi --module cementadmin.wsgi:application --master --processes 1 --die-on-term --socket ${SERVER_HOST}:${SERVER_PORT}"
    uwsgi --module cementadmin.wsgi:application --master --processes 1 --die-on-term --socket ${SERVER_HOST}:${SERVER_PORT}
}

django-server() {
    echo "Running server: python manage.py runserver ${SERVER_HOST}:${SERVER_PORT}"
    python manage.py runserver ${SERVER_HOST}:${SERVER_PORT}
}

run-migrations

case $1 in
    uwsgi-server)
        uwsgi-server
    ;;
    django-server)
        django-server
    ;;
    *)
        if [ $# -eq 0 ]; then
            django-server
        else
            echo "Running command: $@"
            exec $@
        fi
    ;;
esac