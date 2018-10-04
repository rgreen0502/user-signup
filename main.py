from flask import Flask, request, redirect, render_template
import os

app=Flask(__name__)
app.config['DEBUG'] = True

@app.route("/submit-form")
def index():
    return render_template("submission_form.html")


def empty_field(x):
    if x:
        return True
    else:
        return False

def char_length(x):
    if len(x)>2 and len(x)<21:
        return True
    else:
        return False

def at_symbol(x):
    if x.count("@") == 1:
        return True
    else:
        return False

def email_period(x):
    if x.count(".") == 1:
        return True
    else:
        return False

@app.route("/submit-form", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if not empty_field(username):
        username_error="Please enter a Username."

    elif not char_length(username):
        username_error="Must be between 3 and 20 characters."

    else:
        if " " in username:
            username_error="No spaces allowed!"

    if not empty_field(password):
        password_error="Please enter a Password."

    elif not char_length(password):
        password_error="Must be between 3 and 20 characters."

    else:
        if " " in password:
            password_error="No spaces allowed!"

    if verify != password:
        verify_error="Passwords must match."

    if empty_field(email):
        if not char_length(email):
            email_error="Must be between 3 and 20 characters."

        elif not at_symbol(email):
            email_error="Must contain one @ symbol."

        elif not email_period(email):
            email_error="Must contain one dot(.)"

        else:
            if " " in email:
                email_error="No spaces allowed!"

    if not username_error and not password_error and not verify_error and not email_error:
        username=username
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template("submission_form.html", username_error=username_error, username=username, password_error=password_error, password=password, verify=verify, verify_error=verify_error, email_error=email_error, email=email)


@app.route("/welcome")
def good_signup():
    username=request.args.get('username')
    return render_template("welcome.html", username=username)


app.run()