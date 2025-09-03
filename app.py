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

@app.route("/add_form", methods=["GET","POST"])
def add_form():
    return render_template("add.html")

@app.route("/bulk_edit_form", methods= ["GET","POST"])
def bulk_edit_form():
    if request.method == "POST":
        rows = database.show_data()
        for row in rows:
            date = row[0]
            income = request.form.get(f"income_{date}")
            expense = request.form.get(f"expense_{date}")
            saving = request.form.get(f"saving_{date}")

            if income and expense and saving:
                database.edit_data(date, income, expense, saving)  # ✅ use DB helper, not edit_data()

        return redirect(url_for("index"))

    # GET → show table with editable fields
    rows = database.show_data()
    return render_template("bulk_edit.html", rows=rows)

def bulk_edit_save():
    rows = database.show_data()
    for row in rows:
        date = row[0]
        income = request.form.get(f"income_{date}")
        expense = request.form.get(f"expense_{date}")
        saving = request.form.get(f"saving_{date}")

        if income and expense and saving:
            database.edit_data(date, income, expense, saving)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)