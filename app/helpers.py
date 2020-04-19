import os
from flask import Flask, app, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.utils import secure_filename
import sqlite3

from app import app

# Function to handle errors
def apology(message):
    print("Error")
    return render_template("error.html", errorMessage=message)

# Function to add items to box
def packingBox(category, item):

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()

    # Access current user's name
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", [session["user_id"]]
    ).fetchall()

    senderId = session["user_id"]

    # Query database for current package
    currentPackage = db.execute(
        "SELECT * FROM packages WHERE senderId = ? AND status = 0", [senderId]
    ).fetchall()

    # If current package does not exist, create a new package
    if not currentPackage:
        executionCode = (
            "INSERT INTO packages (senderId, senderName, "
            + category
            + ", status) VALUES (?, ?, ?, 0)"
        )
        db.execute(executionCode, [senderId, username[0][0], item])
    # If package already exists, add to it
    else:
        db.execute(
            "UPDATE packages SET "
            + category
            + " = ? WHERE senderId = ? AND status = 0",
            [item, senderId],
        )


# Function to confirm file type
def allowed_image(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False
    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]
    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


# Function to save image to filesystem
def saveImage():

    image = request.files["uploadMeme"]

    if image.filename == "":
        print("No filename")
        return apology("No filename")

    if allowed_image(image.filename):
        # Format name of file
        filename = secure_filename(image.filename)
        # Save to file system and join the path to the uploads folder
        filePath = os.path.join(app.config["IMAGE_UPLOADS"], filename)
        image.save(filePath)
        # Save image path
        imgHTML = "<img src='/static/image-uploads/" + str(filename) + "'>"

    return imgHTML

# Function to categorise boxes
def sortBox(category, tableName):

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()

    receiverId = session["user_id"]

    # Access item in box
    selectItem = (
        "SELECT " + category + " FROM packages WHERE receiverId = ? AND status = 1"
    )

    content = db.execute(selectItem, [receiverId]).fetchall()
    
    # Ensure content exists
    if len(content) == 0:
        content = [[()]]

    if content[0][0]:

        # Access sender information
        senderId = db.execute("SELECT senderId FROM packages WHERE receiverId = ? AND status = 1", [receiverId]).fetchall()[0][0]
        senderUserName = db.execute("SELECT username FROM users WHERE id = ?", [senderId]).fetchall()[0][0]

        # Add to appropriate category database.
        insertItem = "INSERT INTO " + tableName + " VALUES (?, DATE('now'), ?, ?)"
        db.execute(insertItem, [senderId, content[0][0], senderUserName])


# Function to check if there are new boxes
def checkNewBox():

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()
    receiverId = session["user_id"]

    # Access unopened boxes
    unopenBox = db.execute("SELECT * FROM packages WHERE receiverId = ? AND status = 1", [receiverId]).fetchall()

    if len(unopenBox) > 0:
        return True