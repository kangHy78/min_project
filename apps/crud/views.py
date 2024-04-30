from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, login_user, logout_user
from apps.crud.forms import LoginForm, CafeForm
from apps.crud.models import Cafe, Admin
from apps.app import db  


crud = Blueprint(
    "crud",
    __name__,
    template_folder = "templates",
    static_folder = "static"
)



@crud.route("/")
def index():
    return render_template('crud/index.html')

@crud.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        admin = Admin.query.filter_by(username=username).first()
        if admin and admin.password_hash == password : 
            login_user(admin)
            return redirect(url_for("crud.index"))
        
        flash("아이디 또는 비밀번호가 일치하지 않습니다.")
    return render_template("crud/login.html", form=form)


@crud.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("crud.index"))


@crud.route("/cafe_list")
def cafe_list():
    cafes = Cafe.query.all()
    return render_template('crud/cafe_list.html', cafes=cafes)


@crud.route("/add_cafe", methods=["GET", "POST"])
@login_required
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        if request.method == "POST":
            name = request.form["name"]
            address = request.form["address"]
            text = request.form["text"]
            new_cafe = Cafe(name=name, address=address, text=text)
            db.session.add(new_cafe)
            db.session.commit()
            return redirect(url_for("crud.cafe_list"))
        return render_template('crud/add_cafe.html')
    flash("")
    return render_template("crud/add_cafe.html", form=form)



@crud.route("/delete_cafe/<id>", methods=["POST"])
@login_required
def delete_cafe(id):
    cafe_to_delete = Cafe.query.filter_by(id=id).first()
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for("crud.cafe_list"))