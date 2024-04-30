from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired

class LoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired()])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    submit = SubmitField('로그인')

class CafeForm(FlaskForm):
    name = StringField('카페 이름', validators=[InputRequired()])
    address = StringField('카페 주소', validators=[InputRequired()])
    text = TextAreaField('메모 하기')
    submit = SubmitField('추가')     