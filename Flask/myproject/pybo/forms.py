from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DateRequired

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DateRequired('제목은 필수 입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DateRequired('내용은 필수 입력 항목입니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DateRequired('내용은 필수 입력 항목입니다.')])
