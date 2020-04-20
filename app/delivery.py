from app import app

import os
from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.utils import secure_filename
from datetime import datetime
import sqlite3
import random

from app.helpers import apology, packingBox, saveImage, sortBox, checkNewBox

@app.route("/send", methods=["GET", "POST"])
def send():

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()
    # Access current user's name
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", [session["user_id"]]
    ).fetchall()
    userId = session["user_id"]

    if request.method == "POST":

        zoomlife = request.form.get("zoomText")
        video = request.form.get("shareVideo")
        meditation = request.form.get("selectMed")
        message = request.form.get("messageText")

        # Insert into database
        if zoomlife:
            packingBox("zoomlife", zoomlife)

        # Verify that request contains files, i.e. meme
        elif request.files:
            imgHTML = saveImage()
            packingBox("meme", imgHTML)

        elif video:
            video = video.replace("watch?v=", "embed/")
            # Save path to image
            videoHTML = (
                "<iframe width='560' height='315' src='"
                + video
                + "' frameborder='0' allowfullscreen></iframe>"
            )
            packingBox("video", videoHTML)

        elif meditation:
            packingBox("meditation", meditation)

        elif message:
            packingBox("message", message)

        else:
            return apology("You don't seem to have entered anything to add...")

        return redirect("/send")

    else:
        # Access items from row
        boxList = db.execute(
            "SELECT zoomlife, meme, video, meditation, message FROM packages WHERE senderId = ? AND status = 0",
            [userId],
        ).fetchall()

        if not boxList:
            boxList = [()]

        newBox = checkNewBox()

        return render_template("send.html", username=username[0][0], boxList=boxList[0], newBox=newBox)


@app.route("/release")
def release():

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()
    userId = session["user_id"]

    # Choose a random user
    minId = db.execute("SELECT MIN(id) FROM users").fetchall()[0][0]
    maxId = db.execute("SELECT MAX(id) FROM users").fetchall()[0][0]

    # As long as the user is not yourself!
    randomUserId = random.randint(minId, maxId)
    while randomUserId == userId:
        randomUserId = random.randint(minId, maxId)

    # Send to user and set package status to sent (1)
    db.execute(
        "UPDATE packages SET receiverId = ?, status = 1, time = DATE('now') WHERE senderId = ? AND status = 0",
        [randomUserId, userId],
    )

    return redirect("/send")


@app.route("/receive", methods=["GET", "POST"])
def receive():

    # Access database
    database = sqlite3.connect("boxedin.db", isolation_level=None)
    db = database.cursor()
    # Allow access to row names to return dictionary
    db.row_factory = sqlite3.Row
    # Access current user's name
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", [session["user_id"]]
    ).fetchall()
    userId = session["user_id"]

    # When box is opened
    if request.method == "POST":

        # Add items to correct feeds
        sortBox("zoomlife", "zoom")
        sortBox("meme", "memes")
        sortBox("video", "memes")
        sortBox("message", "support")

        # Retrieve box contents
        openBoxId = request.form.get("selectBox")

        openBoxContents = db.execute("SELECT zoomlife, meme, video, meditation, message FROM packages WHERE packageId = ?", [openBoxId]).fetchall()[0]

        sender = db.execute("SELECT senderName FROM packages WHERE packageId = ?", [openBoxId]).fetchall()[0][0]

        time = db.execute("SELECT time FROM packages WHERE packageId = ?", [openBoxId]).fetchall()[0][0]

        # Set box status to opened (2)
        db.execute("UPDATE packages SET status = 2 WHERE receiverId = ? AND status = 1", [userId])

        # Check database for received boxes and show as dictionary
        deliveries = db.execute("SELECT * FROM packages WHERE receiverId = ? ORDER BY packageId DESC", [userId]).fetchall()
        deliveries = [dict(row) for row in deliveries]

        return render_template("receive.html", username=username[0][0], openBox=openBoxContents, sender=sender, time=time, deliveries=deliveries)

    else:

        # Check database for received boxes and show as dictionary
        deliveries = db.execute("SELECT * FROM packages WHERE receiverId = ? ORDER BY packageId DESC", [userId]).fetchall()
        deliveries = [dict(row) for row in deliveries]

        # Display received boxes
        return render_template("receive.html", username=username[0][0], deliveries=deliveries)
