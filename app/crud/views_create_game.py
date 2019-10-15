from app.crud import crud
from flask import render_template, request, jsonify
from app.forms import GameAddForm
from app.orm import ORM
from app.models import Game
from app.crud.views_common import dt


@crud.route("/create/game/", methods=("GET", "POST"))
def create_game():
    data = dict(
        title="新增大賽"
    )
    if request.method == "POST":
        res = dict(code=0)
        form = GameAddForm()
        if form.validate():
            save_game(form)
            res['code'] = 1
        else:
            res = form.errors
            res["code"] = 0
        return jsonify(res)
    else:
    	return render_template("create_game.html", data=data)


def save_game(form):
    session = ORM.db()
    try:
        game = Game(
            name=form.name.data,
            email=form.email.data,
            createdAt=dt(),
            updatedAt=dt()
        )
        session.add(game)
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    return
