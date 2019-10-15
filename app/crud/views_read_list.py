# -*- coding: utf-8 -*-
from app.crud import crud
from flask import render_template
from app.orm import ORM
from app.models import Game
from app.crud.views_common import page
from sqlalchemy import func
from app.params import *



@crud.route("/", methods=("GET", "POST"))
@crud.route("/read/list/", methods=("GET", "POST"))
def read_list():
    data = dict(
        title="賽事列表"
    )
    arr = None
    session = ORM.db()
    try:
        model = session.query(Game).order_by(Game.id.desc())
        arr = page(model)

    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    data["arr"] = arr
    return render_template("read_list.html", data=data)

