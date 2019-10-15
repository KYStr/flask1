from app.crud import crud
from flask import render_template, request, jsonify, redirect
from app.forms import MessageAddForm
from app.orm import ORM
from app.models import Game, Message
from app.crud.views_common import dt, get_gam


@crud.route("/add/message/", methods=("GET", "POST"))
def add_message():
    id = request.args.get("id", None)

    data = dict(
        title="新增公告"
    )
    if request.method == "POST":
        res = dict(code=0)
        form = MessageAddForm()
        if form.validate():
            save_message(form)
            res['code'] = 1
        else:
            res = form.errors
            res["code"] = 0
        return jsonify(res)
    else:
        if id:
            data["gam"] = get_gam(id)
            return render_template("add_message.html", data=data)
        else:
            return redirect(url_for('crud.read_one', id=id))



def save_message(form):
    session = ORM.db()
    try:
        message = Message(
            game_id=form.id.data,
            title=form.name.data,
            content=form.info.data,
            createdAt=dt(),
            updatedAt=dt()
        )
        session.add(message)
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    return
