import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from datetime import datetime
import sqlite3
import re
import random

# Initalise app variable
app = Flask(__name__)

# Import other files
from app import user
from app import feeds
from app import delivery
from app.helpers import apology

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = b"t\x98\xf4\x13&z\xaf\xdc\x12s\xac\xb0\xee\xa2\xb9\xb7"

# Specify directory to store files
app.config["IMAGE_UPLOADS"] = "/Users/michellelo/Desktop/Boxed-In/app/static/image-uploads"

# Specify allowed file types for uploads
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]

# Maximum file size of 50 megabytes
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

# Connect to database
db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()

# Create tables
db.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, passhash TEXT)"
)
db.execute(
    "CREATE TABLE IF NOT EXISTS packages (packageId INTEGER PRIMARY KEY AUTOINCREMENT, senderId INTEGER, senderName TEXT, receiverId INTEGER, zoomlife TEXT, meme TEXT, video TEXT, meditation TEXT, message TEXT, time DATETIME, status INTEGER)"
)
db.execute(
    "CREATE TABLE IF NOT EXISTS zoom (senderId INTEGER, time DATETIME, zoomlife TEXT, senderName TEXT)"
)
db.execute(
    "CREATE TABLE IF NOT EXISTS memes (senderId INTEGER, time DATETIME, memelink TEXT, senderName TEXT)"
)
db.execute(
    "CREATE TABLE IF NOT EXISTS support (senderId INTEGER, time DATETIME, support TEXT, senderName TEXT)"
)

# Error handling
@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	return apology("Sorry, we couldn't find that page."), 404

@app.errorhandler(500)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	return apology("Sorry, there was a server error."), 500
