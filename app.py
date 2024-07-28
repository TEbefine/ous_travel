import os
import bcrypt

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///informations.db")

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    if 'user_name' in session:
        return render_template("index.html", name=session["user_name"])
    else:
        return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        # Check not type in
        if not request.form.get("username"):
            return render_template("login.html", problems="type in ID")
        if not request.form.get("password"):
            return render_template("login.html", problems="type in password")
        
        username = request.form.get("username")
        check_username = db.execute("SELECT username FROM users WHERE username=?", username)
        if not check_username:
            return render_template("login.html", problems="ID isn't exis!")
        
        password = request.form.get("password")
        rows = db.execute("SELECT * FROM users WHERE username=?", username)

        if not bcrypt.checkpw(password.encode('utf-8'), rows[0]["hash"]):
            return render_template("login.html", problems="Password don't correct!")
        
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["user_name"] = rows[0]["name"]

        # Redirect user to home page
        return redirect("/")
    
    else:
        if 'user_name' in session:
            return redirect("/profile")
        else:
            return render_template("login.html")
    
@app.route("/logout")
def logout():

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        # Check not type in
        if not request.form.get("username"):
            return render_template("register.html", problems="type in your ID")
        elif not request.form.get("username").isalnum():
            return render_template("register.html", problems="type just only letter or number")
        if not request.form.get("password"):
            return render_template("register.html", problems="type in your Password")
        elif not request.form.get("password").isalnum():
            return render_template("register.html", problems="type just only letter or number in password")
        if not request.form.get("confirmation"):
            return render_template("register.html", problems="type in your Confirmation")
        if not request.form.get("name"):
            return render_template("register.html", problems="type in your Name")
        elif not request.form.get("name").isalnum():
            return render_template("register.html", problems="letter or number your name")
        
        # Check correct same password
        password = request.form.get("password")
        check_password = request.form.get("confirmation")
        if not password == check_password:
            return render_template("register.html", problems="password not correct!")
        
        # Username has been used our not
        username = request.form.get("username")
        check_username = db.execute("SELECT username FROM users WHERE username=?", username)
        if check_username:
            return render_template("register.html", problems="username has been already exis!")
        
        # Store information
        name = request.form.get("name")
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        db.execute("INSERT INTO users (name, username, hash) VALUES (?, ?, ?)", name, username, hashed)

        rows = db.execute("SELECT * FROM users WHERE username=?", username)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["user_name"] = rows[0]["name"]

        # Redirect user to home page
        return redirect("/")
    
    else:
        return render_template("register.html")
    
@app.route("/central_trip")
def central():

    if 'user_name' in session:
        return render_template("central_trip.html", name=session["user_name"])
    else:
        return render_template("central_trip.html")
    
@app.route("/extra_trip")
def extra():

    if 'user_name' in session:
        return render_template("extra_trip.html", name=session["user_name"])
    else:
        return render_template("extra_trip.html")
    
@app.route("/profile")
def profile():

    if 'user_name' in session:
        if session["user_id"] == 3:
            num_users = db.execute("SELECT COUNT(*) AS num FROM users")

            degrees = db.execute("SELECT id_trip, COUNT(*) AS count FROM reserve GROUP BY id_trip ORDER BY count DESC")

            ratings = []
            rating = 1
            prev_count = degrees[0]["count"]
            for i in range(len(degrees)):
                new_dict = degrees[i].copy()
                if degrees[i]["count"] != prev_count:
                    rating += 1
                new_dict["rating"] = rating
                new_dict["region"] = db.execute("SELECT region FROM trip WHERE id=?", degrees[i]["id_trip"])[0]["region"]
                ratings.append(new_dict)
                prev_count = degrees[i]["count"]

            users = db.execute("SELECT id, name FROM users")

            for user in users:
                trips = db.execute("SELECT id_trip FROM reserve WHERE id_user=?", user["id"])

                regions = []
                if trips:
                    for trip in trips:
                        regions.append(db.execute("SELECT region FROM trip WHERE id=?", trip["id_trip"])[0]["region"])
                user["region"] = ', '.join(regions)
                
            users = [user for user in users if user["region"]]

            return render_template("profile.html", name=session["user_name"], num=num_users[0]["num"], ratings=ratings, users=users)
        
        reserves = db.execute("SELECT * FROM reserve WHERE id_user=?", session["user_id"])
        if not reserves:
            return render_template("profile.html", name=session["user_name"])
        else:
            total_price = 0
            for reserve in reserves:
                total_price += reserve["price"]
                region = db.execute("SELECT region FROM trip WHERE id=?", reserve["id_trip"])
                reserve["region"] = region[0]
            
            total = f"${total_price:,.0f}"

            return render_template("profile.html", name=session["user_name"], reserves=reserves, total=total)
    else:
        return redirect("/login")
    
@app.route("/reserve", methods=["POST"])
def reserve():

    if not request.form.get("id"):
        flash("This option is only available in certain situations.")
        return redirect("/profile")
    
    if request.form.get("id") == "349":
        check_beppu = db.execute("SELECT * FROM reserve WHERE id_user=? AND id_trip=1001", session["user_id"])
        beppu_trip = db.execute("SELECT * FROM trip WHERE id=1001")

        if not check_beppu:
            beppu_trip[0]["price"] += 349
            beppu_trip[0]["phrase"] += " Find serenity in the soothing rhythm of the sea."

            db.execute("INSERT INTO reserve (id_user, id_trip, price, phrase) VALUES (?, ?, ?, ?)", session["user_id"], beppu_trip[0]["id"], beppu_trip[0]["price"], beppu_trip[0]["phrase"])
            flash("Thank you for your reservation. Your booking has been confirmed.")
            return redirect("/profile")
        else:
            if check_beppu[0]["price"] == 1948:
                flash("Your plus trip is now confirmed.")
                return redirect("/profile")
            
            check_beppu[0]["price"] += 349
            check_beppu[0]["phrase"] += " Find serenity in the soothing rhythm of the sea."

            db.execute("UPDATE reserve SET price = ?, phrase = ? WHERE id_user=? AND id_trip=1001", check_beppu[0]["price"], check_beppu[0]["phrase"], session["user_id"])
            flash("Your trip changes have been confirmed.")
            return redirect("/profile")

    if request.form.get("id") == "149":
        print(request.form.get("id"))
        check_nagasaki = db.execute("SELECT * FROM reserve WHERE id_user=? AND id_trip=1002", session["user_id"])
        nagasaki_trip = db.execute("SELECT * FROM trip WHERE id=1002")

        if not check_nagasaki:
            nagasaki_trip[0]["price"] += 149
            nagasaki_trip[0]["phrase"] += " Unleash your creativity through the art of clay."

            db.execute("INSERT INTO reserve (id_user, id_trip, price, phrase) VALUES (?, ?, ?, ?)", session["user_id"], nagasaki_trip[0]["id"], nagasaki_trip[0]["price"], nagasaki_trip[0]["phrase"])
            flash("Thank you for your reservation. Your booking has been confirmed.")
            return redirect("/profile")
        else:
            if check_nagasaki[0]["price"] == 1448:
                flash("Your plus trip is now confirmed.")
                return redirect("/profile")
            
            check_nagasaki[0]["price"] += 149
            check_nagasaki[0]["phrase"] += " Unleash your creativity through the art of clay."

            db.execute("UPDATE reserve SET price = ?, phrase = ? WHERE id_user=? AND id_trip=1002", check_nagasaki[0]["price"], check_nagasaki[0]["phrase"], session["user_id"])
            flash("Your trip changes have been confirmed.")
            return redirect("/profile")
        
    check_id = db.execute("SELECT * FROM trip WHERE id=?", request.form.get("id"))

    if not check_id:
        flash("This option is only available in certain situations.")
        return redirect("/profile")

    check_duplicate = db.execute("SELECT id_trip FROM reserve WHERE id_user=? AND id_trip=?", session["user_id"], request.form.get("id"))

    if check_duplicate:
        flash("You're all set for your adventure!")
        return redirect("/profile")
    
    trip_data = db.execute("SELECT * FROM trip WHERE id=?", request.form.get("id"))

    db.execute("INSERT INTO reserve (id_user, id_trip, price, phrase) VALUES (?, ?, ?, ?)", session["user_id"], trip_data[0]["id"], trip_data[0]["price"], trip_data[0]["phrase"])

    flash("Thank you for your reservation. Your booking has been confirmed.")
    return redirect("/profile")   

@app.route("/cancelled", methods=["POST"])
def cancelled():

    if not request.form.get("id"):
        flash("This option is only available in certain situations.")
        return redirect("/profile")
    
    check_id = db.execute("SELECT * FROM reserve WHERE id_user=? AND id_trip=?", session["user_id"], request.form.get("id"))

    if not check_id:
        flash("This option is only available in certain situations.")
        return redirect("/profile")

    db.execute("DELETE FROM reserve WHERE id_user=? AND id_trip=?", session["user_id"], request.form.get("id"))

    flash("Your cancellation request has been processed.")
    return redirect("/profile")
