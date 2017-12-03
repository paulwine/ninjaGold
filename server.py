from flask import Flask, redirect, request, session, flash, render_template
import random

app = Flask(__name__)

app.secret_key = "SECRETS"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods =["POST"])
def addCoins():
    session["name"] = request.form.keys()[0]
    if "wallet" not in session:
        session["wallet"] = 0
    

    if session["name"] == "farm":
        session["num"] = random.randint(10,21)
        flash("Nice farming.  You get " + str(session["num"]) + " coins.")
        print("Nice farming.  You get " + str(session["num"]) + " coins.")
        session["wallet"] += session["num"]
        flash("You have " + str(session["wallet"]) +" coins in your wallet")
        print("You have " + str(session["wallet"]) +" coins in your wallet")
        return redirect("/")
    elif session["name"] == "cave":
        session["num"] = random.randint(5,10)
        flash("Nice spelunking.  You get " + str(session["num"]) + " coins.")
        print("Nice spelunking.  You get " + str(session["num"]) + " coins.")
        session["wallet"] += session["num"]
        flash("You have " + str(session["wallet"]) + " coins in your wallet")
        print("You have " + str(session["wallet"])  +" coins in your wallet")
        return redirect("/")
    elif session["name"] == "house":
        session["num"] = random.randint(2,5)
        flash("Nice job laying around like a bum.  You get " + str(session["num"]) + " coins.")
        print("Nice job laying around like a bum.  You get " + str(session["num"]) + " coins.")
        session["wallet"] += session["num"]
        flash("You have " + str(session["wallet"]) +" coins in your wallet")
        print("You have " + str(session["wallet"]) +" coins in your wallet")
        return redirect("/")
    elif session["name"] == "casino":
        session["num"] = random.randint(-50,50)
        if session["wallet"] <= 0:
            flash("You have no more money.  The casino people and loan sharks are going to track you down and break your knees and your family will live in poverty.  Were all those drunken nights at the casino really worth it?  You were such an honorable ninja, and now you have nothing.")
            print("You have no more money.  The casino people and loan sharks are going to track you down and break your knees and your family will live in poverty.  Were all those drunken nights at the casino really worth it?  You were such an honorable ninja, and now you have nothing.")
            return redirect("/")
        elif session["wallet"]>0:
            if session["num"] < 0:
                flash("Stop gambling, you have a Problem.  You lose " + str(session["num"]) + " coins.")
                print("Stop gambling, you have a Problem.  You lose " + str(session["num"]) + " coins.")
                session["wallet"] += session["num"]
                flash("You have " + str(session["wallet"]) +" coins in your wallet")
                print("You have " + str(session["wallet"]) +" coins in your wallet")
                return redirect("/")
            elif session["num"] > 0:
                flash("You lucky Dog.  You win " + str(session["num"]) + " coins.")
                print("You lucky Dog.  You win " + str(session["num"]) + " coins.")
                session["wallet"] += session["num"]
                flash("You have " + str(session["wallet"]) +" coins in your wallet")
                print("You have " + str(session["wallet"]) +" coins in your wallet")
                return redirect("/")
            elif session["num"] == 0:
                flash("You broke even.  No coins for you")
                print("You broke even.  No coins for you")
                session["wallet"] += session["num"]
                flash("You have " + str(session["wallet"]) +" coins in your wallet")
                print("You have " + str(session["wallet"]) +" coins in your wallet")
                return redirect("/")

    

    else:    
        return redirect("/")

app.run(debug=True)