#!/bin/sh

cd code
# run Celery worker for our project rssscrapper with Celery configuration stored in Celeryconf
sh -c "celery -A rssscrapper worker -l info"
