from flask import Flask
import cv2
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/uploads'
app.config.from_object('config')

from app import routes
