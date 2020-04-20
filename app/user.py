from app import app
from app.helpers import apology

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
import re

# Landing page
@app.route("/")
def index():
    return render_template("index.html")

# Sign up
@app.route("/register", methods=["GET", "POST"])
def register():

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()

    # User registers in form
    if request.method == "POST":

        usernameInput = request.form.get("username")
        email = request.form.get("email")
        passwordInput = request.form.get("password")
        confirmPass = request.form.get("confirmation")

        # Query database for username
        userMatches = db.execute(
            "SELECT * FROM users WHERE username = ?", [str(usernameInput)]
        ).fetchall()

        # Check for existing users
        if len(userMatches) > 0:
            return apology("That username already exists.")

        # If username field is blank
        if not usernameInput:
            return apology("Please enter a username.")

        # If email field is blank
        if not email:
            return apology("Please enter an email address.")

        # Check if email is school email
        domain = re.search("@[\w.-]+", email)
        domain = str(domain.group())

        if domain != "@sec.ycis-hk.com" and domain != "@hk.ycef.com":
            return apology("Please enter a YCIS HK school email address.")

        # If password fields are blank
        if not passwordInput or not confirmPass:
            return apology("Please enter your password twice.")

        # If confirmation does not match
        if passwordInput != confirmPass:
            return apology("Your password and confirmation do not match.")

        # Count characters and letters in password
        passwordLetters = sum(c.isalpha() for c in passwordInput)
        passwordNumbers = sum(c.isdigit() for c in passwordInput)

        # Match conditions
        if len(passwordInput) < 8 or passwordLetters < 3 or passwordNumbers < 3:
            return apology("Your password is not secure.")

        # Insert the new user into users, storing a hash of the user’s password, not the password itself
        passwordHash = generate_password_hash(passwordInput)

        insertDataUsers = [str(usernameInput), str(email), str(passwordHash)]
        db.execute(
            "INSERT INTO users (username, email, passhash) VALUES (?, ?, ?)", insertDataUsers
        )

        # Introduce Boxed In
        return render_template("introduction.html")

    else:

        return render_template("register.html")

# Log In
@app.route("/login", methods=["GET", "POST"])
def login():

    # Access database
    db = sqlite3.connect("boxedin.db", isolation_level=None).cursor()

    # User registers in form
    if request.method == "POST":

        usernameInput = request.form.get("username")
        passwordInput = request.form.get("password")
        confirmPass = request.form.get("confirmation")

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Please provide a username.")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Please provide a password.")

        # Query database for username
        userMatches = db.execute(
            "SELECT * FROM users WHERE username = ?", [str(usernameInput)]
        ).fetchall()

        # Ensure username exists and password is correct
        if len(userMatches) != 1 or not check_password_hash(
            userMatches[0][3], passwordInput
        ):
            return apology("Invalid username and/or password.")

        # Remember which user has logged in
        session["user_id"] = userMatches[0][0]

        # Redirect user to home page
        return redirect("/zoomlife")

    else:
        return render_template("login.html")

# Logout
@app.route("/logout")
def logout():

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# Rules
@app.route("/rules")
def rules():
    return render_template("rules.html")