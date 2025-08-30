from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

@app.route("/")
def index():
    data = database.show_data()
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add():
    date=request.form["date"]
    income=request.form["income"]
    expense=request.form["expense"]
    saving=request.form["saving"]
    database.add_data(date, income, expense, saving)
    return redirect(url_for("index"))

@app.route("/edit", methods=["POST"])
def edit():
    date=request.form["date"]
    income=request.form["income"]
    expense=request.form["expense"]
    saving=request.form["saving"]
    database.edit_data(date, income, expense, saving)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)