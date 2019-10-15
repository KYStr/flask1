# -*- coding: utf-8 -*-
from app.crud import crud
from flask import redirect, url_for, request, render_template, jsonify
from app.models import Game, Message
from app.orm import ORM
from app.forms import MessageEditForm
from app.crud.views_common import dt, get_gam
from sqlalchemy import and_


@crud.route("/update/message/", methods=("GET", "POST"))
def update_message():
    id = request.args.get("id", None)
    game_id = request.args.get("game_id", None)

    data = dict(
        title="公告修改"
    )
    if request.method == "POST":
        res = dict(code=0)
        form = MessageEditForm()
        if form.validate():
            update_mes(form)
            res["code"] = 1
        else:
            res = form.errors
            res["code"] = 0
        return jsonify(res)
    else:
        if id:
            data['mes'] = get_mes(id)
            return render_template("update_message.html", data=data)
        else:
            return redirect(url_for('crud.read_one', id=game_id))


def get_mes(id):
    session = ORM.db()
    emp, hob = None, None
    try:
        mes = session.query(Message).filter_by(id=int(id)).first()
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    return mes


def update_mes(form):
    session = ORM.db()
    try:
        # 修改員工訊息
        emp = session.query(Message).filter_by(id=int(form.id.data)).first()
        #emp.game_id = form.game_id.data
        emp.content = form.info.data
        emp.title = form.name.data
        emp.updatedAt = dt()
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
