# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms.fields import StringField, IntegerField, SelectField, DateField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp
from app.params import *


# 錄入員工表單
class EmployeeAddForm(Form):
    name = StringField(
        "姓名",
        validators=[
            DataRequired("姓名不能為空!")
        ]
    )
    job = SelectField(
        "職位",
        choices=[(k + 1, v) for k, v in enumerate(job_list)],
        coerce=int,
        validators=[
            DataRequired("職位不能為空!")
        ]
    )
    sex = SelectField(
        "性別",
        choices=[(k + 1, v) for k, v in enumerate(sex_list)],
        coerce=int,
        validators=[
            DataRequired("性別不能為空!")
        ]
    )
    edu = SelectField(
        "學歷",
        choices=[(k + 1, v) for k, v in enumerate(edu_list)],
        coerce=int,
        validators=[
            DataRequired("學歷不能為空!")
        ]
    )
    birth = DateField(
        "生日",
        validators=[
            DataRequired("生日不能為空!")
        ]
    )
    email = StringField(
        "郵箱",
        validators=[
            DataRequired("郵箱不能為空!"),
            Email("郵箱格式不正確!!")
        ]
    )
    phone = StringField(
        "手機",
        validators=[
            DataRequired("手機不能為空!"),
            Regexp("09\\d{8}", message="手機格是不正確!")
        ]
    )
    hobby = SelectMultipleField(
        "愛好",
        choices=[(k + 1, v) for k, v in enumerate(edu_list)],
        coerce=int,
        validators=[
            DataRequired("愛好不能為空!")]
    )
    info = TextAreaField(
        u"介紹",
        validators=[
            DataRequired(u"介紹不能為空!")
        ]
    )
    face = StringField(
        "頭像",
        validators=[
            DataRequired("頭像不能為空!")
        ]
    )


# 修改員工表單
class EmployeeEditForm(Form):
    id = IntegerField(
        "編號",
        validators=[
            DataRequired("編好不能為空!")
        ]
    )
    name = StringField(
        "姓名",
        validators=[
            DataRequired("姓名不能為空!")
        ]
    )
    job = SelectField(
        "職位",
        choices=[(k + 1, v) for k, v in enumerate(job_list)],
        coerce=int,
        validators=[
            DataRequired("職位不能為空!")
        ]
    )
    sex = SelectField(
        "性別",
        choices=[(k + 1, v) for k, v in enumerate(sex_list)],
        coerce=int,
        validators=[
            DataRequired("性別不能為空!")
        ]
    )
    edu = SelectField(
        "學歷",
        choices=[(k + 1, v) for k, v in enumerate(edu_list)],
        coerce=int,
        validators=[
            DataRequired("學歷不能為空!")
        ]
    )
    birth = DateField(
        "生日",
        validators=[
            DataRequired("生日不能為空!")
        ]
    )
    email = StringField(
        "郵箱",
        validators=[
            DataRequired("郵箱不能為空!"),
            Email("郵箱格式不正確!!")
        ]
    )
    phone = StringField(
        "手機",
        validators=[
            DataRequired("手機不能為空!"),
            Regexp("09\\d{8}", message="手機格是不正確!")
        ]
    )
    hobby = SelectMultipleField(
        "愛好",
        choices=[(k + 1, v) for k, v in enumerate(edu_list)],
        coerce=int,
        validators=[
            DataRequired("愛好不能為空!")]
    )
    info = TextAreaField(
        u"介紹",
        validators=[
            DataRequired(u"介紹不能為空!")
        ]
    )
    face = StringField(
        "頭像",
        validators=[
            DataRequired("頭像不能為空!")
        ]
    )

# 錄入大賽表單
class GameAddForm(Form):
    name = StringField(
        "大賽名稱",
        validators=[
            DataRequired("大賽名稱不能為空!")
        ]
    )
    email = StringField(
        "郵箱",
        validators=[
            DataRequired("郵箱不能為空!"),
            Email("郵箱格式不正確!!")
        ]
    )

# 錄入比賽表單
class SubgameAddForm(Form):
    id = IntegerField(
        "大賽編號",
        validators=[
            DataRequired("大賽編號不能為空!")
        ]
    )
    name = StringField(
        "比賽名稱",
        validators=[
            DataRequired("比賽名稱不能為空!")
        ]
    )
    url = StringField(
        "比賽連結",
        validators=[
            DataRequired("比賽連結不能為空!"),
        ]
    )
    img = StringField(
        "比賽圖片",
        validators=[
            DataRequired("比賽圖片不能為空!")
        ]
    )

# 錄入公告表單
class MessageAddForm(Form):
    id = IntegerField(
        "大賽編號",
        validators=[
            DataRequired("大賽編號不能為空!")
        ]
    )
    name = StringField(
        "公告標題",
        validators=[
            DataRequired("公告標題不能為空!")
        ]
    )
    info = TextAreaField(
        u"內容",
        validators=[
            DataRequired(u"內容不能為空!")
        ]
    )

# 修改公告表單
class MessageEditForm(Form):
    id = IntegerField(
        "id",
        validators=[
            DataRequired("id不能為空!")
        ]
    )    
    game_id = IntegerField(
        "大賽編號",
        validators=[
            DataRequired("大賽編號不能為空!")
        ]
    )
    name = StringField(
        "公告標題",
        validators=[
            DataRequired("公告標題不能為空!")
        ]
    )
    info = TextAreaField(
        u"內容",
        validators=[
            DataRequired(u"內容不能為空!")
        ]
    )

# 錄入菜單表單
class MenuAddForm(Form):
    id = IntegerField(
        "大賽編號",
        validators=[
            DataRequired("大賽編號不能為空!")
        ]
    )
    name = StringField(
        "菜單",
        validators=[
            DataRequired("菜單不能為空!")
        ]
    )
    url = StringField(
        "連結",
        validators=[
            DataRequired("連結不能為空!"),
        ]
    )
