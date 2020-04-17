from app import app

from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import sqlite3

from app.helpers import apology, checkNewBox

@app.route("/zoomlife")
def zoomlife():

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()

    # Access current user's name
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", [session["user_id"]]
    ).fetchall()

    newBox = checkNewBox()

    # Access all #zoomlife posts
    zoomLifePosts = db.execute("SELECT * FROM zoom ORDER BY time DESC").fetchall()

    if not zoomLifePosts:
        zoomLifePosts = [("", "", "No posts yet. Add one now!", "Oh no...")]

    return render_template(
        "zoomlife.html", username=username[0][0], zoomLifePosts=zoomLifePosts, newBox=newBox
    )


@app.route("/memes")  # TO DO AFTER UPLOADING
def memes():

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()

    # Access current user's name
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", [session["user_id"]]
    ).fetchall()

    newBox = checkNewBox()

    # Access all meme posts
    memePosts = db.execute("SELECT * FROM memes ORDER BY time DESC").fetchall()

    if not memePosts:
        memePosts = [("", "", "No posts yet. Add one now!", "Oh no...")]

    return render_template("memes.html", username=username[0][0], memePosts=memePosts, newBox=newBox)


@app.route("/meditations")
def meditations():

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()

    # Access current user's name
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", [session["user_id"]]
    ).fetchall()

    newBox = checkNewBox()

    if not username:
        username = [("", "", "No posts yet. Add one now!", "Oh no...")]

    return render_template("meditations.html", username=username[0][0], newBox=newBox)


@app.route("/support")
def support():

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()

    # Access current user's name
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", [session["user_id"]]
    ).fetchall()

    newBox = checkNewBox()

    # Access all #zoomlife posts
    supportPosts = db.execute("SELECT * FROM support ORDER BY time DESC").fetchall()

    if not supportPosts:
        supportPosts = [("", "", "No posts yet. Add one now!", "Oh no...")]

    return render_template(
        "support.html", username=username[0][0], supportPosts=supportPosts, newBox=newBox
    )
