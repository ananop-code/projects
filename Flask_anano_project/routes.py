from ext import app, db
from flask import render_template, redirect
from forms import RegisterForm, HistoryForm
from models import History
from os import path


profiles = []


@app.route("/")
def home():
    histories = History.query.filter(history.year < 2026).all()
    return render_template("index.html",
                           histories=histories, role="admin")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {
            "username": form.username.data,
            "mobile": form.mobile.data,
            "date": form.birthdate.data,
        }
        img = form.image.data # None <FileStorage screen>
        if img:
            directory = path.join(app.root_path, "static", "images", img.filename)
            new_user["img"] = img.filename
            img.save(directory)
        profiles.append(new_user)
        return redirect("/")
    return render_template("register.html", form=form)


@app.route("/add_information", methods=["GET", "POST"])
def add_movie():
    form = HistoryForm()
    if form.validate_on_submit():
        new_history = History(title=form.title.data, year=form.year.data)
        img = form.image.data
        new_history.image = img.filename

        directory = path.join(app.root_path, "static", "images", img.filename)
        img.save(directory)

        db.session.add(new_history)
        db.session.commit()
        return redirect("/")
    return render_template("add_information.html", form=form)




@app.route("/delete_history/<int:history_id>")
def delete_history(history_id):
    history = History.query.get(history_id)
    db.session.delete(history)
    db.session.commit()
    return redirect("/")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/history/<int:history_id>")
def view_history_details(history_id):
    history = History.query.get(history_id)
    return render_template("history_details.html", history=history)

