import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    others = request.form.get("selfless")
    religion = request.form.get("religion")
    god = request.form.get("god")
    politics = request.form.get("politics")
    celebrities = request.form.get("celebrities")
    culture = request.form.get("culture")
    thinking = request.form.get("thinking")
    shock = request.form.get("shock")
    lesson = request.form.get("lesson")
    parody = request.form.get("parody")

    if not others or not religion or not God or not politics or not celebrities or not culture or not thinking or not shock or not lesson or not parody:
        return render_template("error.html", message="get it together!")

    else:
        with open("survey.csv", "a", newline="") as file:
            columns = ["name", "team", "position"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow({"name": name, "team": team, "position": position})
        return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    with open("survey.csv") as file:
        reader = csv.DictReader(file)

        data = list(reader)

        if not data:
            return render_template("error.html", message="not enough players to field a team")

        else:
            return render_template("sheet.html", data=data)

