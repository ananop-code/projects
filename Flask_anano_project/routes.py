from ext import app, db
from flask import render_template, redirect , flash
from forms import RegisterForm, HistoryForm, LoginForm
from models import History, User
from flask_login import login_user, logout_user, login_required
from os import path


profiles = []


@app.route("/")
def home():
    histories = History.query.filter(History.year < 2026).all()
    return render_template("index.html",
                           histories=histories, role="admin")
@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user:
            login_user(user)
            flash("succesfully logged in")
            return redirect("/")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")



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
def add_information():
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


@app.route("/update_information/<int:history_id>", methods=["GET", "POST"])
@login_required
def update_information(history_id):
    history = History.query.get(history_id)
    form = HistoryForm(title=history.title, year=history.year)
    if form.validate_on_submit():
        history.title = form.title.data
        history.year = form.year.data
        image = form.image.data # None თუ წერია შიგნით რამე
        if image:
            directory = path.join(app.root_path, "static", "images", image.filename)
            image.save(directory)
            history.image = image.filename

        history.save()
        return redirect("/")
    return render_template("add_information.html", form=form)




@app.route("/delete_history/<int:history_id>")
def delete_history(history_id):
    history = History.query.get(history_id)
    db.session.delete(history)
    return redirect("/")




@app.route("/history/<int:history_id>")
def view_history_details(history_id):
    history = History.query.get(history_id)
    return render_template("history_details.html", history=history)

