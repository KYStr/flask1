# -*- coding: utf-8 -*-
import os
import math
import datetime
import uuid
from app.crud import crud
from app.params import *
from flask import request, jsonify
from werkzeug.utils import secure_filename
from app.orm import ORM
from app.models import Game

# 定義上下文處理器
@crud.context_processor
def data_params():
    return dict(
        job_list=job_list,
        edu_list=edu_list,
        sex_list=sex_list,
        hobby_list=hobby_list,
        job_param=enumerate(job_list),
        edu_param=enumerate(edu_list),
        sex_param=enumerate(sex_list),
        hobby_param=enumerate(hobby_list),
    )

# 文件上傳視圖

# 指定上傳目錄
upload_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "static/uploads"
)
# 指定允許後綴名 EX .jpg .jpeg .png .gif .bmp
allowed_ext = set(["jpg", "jpeg", "gif", "png"])


# 文件後綴名判斷
def allowed_file(filename):
    # 1. .文件名
    # 2. 以最右邊的.作為分割數組，獲取最後數值轉為小寫並比較
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_ext


# 文件上傳接口
@crud.route("/upload/", methods=("POST",))
def upload():
    file = request.files['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filename = "{}{}{}".format(
            datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            uuid.uuid4().hex,
            os.path.splitext(filename)[-1]
        )
        file.save(os.path.join(upload_path, filename))
        return jsonify(
            dict(
                code=1,
                image=filename
            )
        )

def dt():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 分頁效果
def page(model):
    page = request.args.get("page", 1)  # 獲取頁碼
    page = int(page)
    total = model.count()  # 獲取總紀錄數
    if total:
        shownum = 10  # 每頁顯示條目
        pagenum = int(math.ceil(total / shownum))  # 总的页数
        if page < 1:
            page = 1
        if page > pagenum:
            page = pagenum
        offset = (page - 1) * shownum
        data = model.limit(shownum).offset(offset).all()
        prev_p = page - 1
        next_p = page + 1
        if prev_p < 1:
            prev_p = 1
        if next_p > pagenum:
            next_p = pagenum
        arr = dict(
            pagenum=pagenum,
            total=total,
            prev=prev_p,
            next=next_p,
            data=data,
            page=page
        )
    else:
        arr = dict(
            data=[]
        )
    return arr


def get_gam(id):
    session = ORM.db()
    gam = None
    try:
        gam = session.query(Game).filter_by(id=int(id)).first()
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    return gam
