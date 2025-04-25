# importing necessary modules
from flask import Flask, request, jsonify
from celery import Celery
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector
from mysql.connector import error
from datetime import datetime

# load environment variables
load_dotenv()

# celery configuration
app.config['CELERY_BROKER_URL'] = os.getenv('REDIS_URL')
app.config['CELERY_RESULT_BACKEND'] = os.getenv('REDIS_URL')

# initialize celery
celery = Celery(
    app.name, 
    broker = app.config['CELERY_BROKER_URL'],
    backend = app.config['CELERY_RESULT_BACKEND']
)

celery.conf.update(app.config)


