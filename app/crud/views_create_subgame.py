from app.crud import crud
from flask import render_template, request, jsonify, redirect
from app.forms import SubgameAddForm
from app.orm import ORM
from app.models import Game, Subgame
from app.crud.views_common import dt, get_gam


@crud.route("/create/subgame/", methods=("GET", "POST"))
def create_subgame():
    id = request.args.get("id", None)

    data = dict(
        title="新增比賽項目"
    )
    if request.method == "POST":
        res = dict(code=0)
        form = SubgameAddForm()
        if form.validate():
            save_subgame(form)
            res['code'] = 1
        else:
            res = form.errors
            res["code"] = 0
        return jsonify(res)
    else:
        if id:
            data["gam"] = get_gam(id)
            return render_template("create_subgame.html", data=data)
        else:
            return redirect(url_for('crud.read_one', id=id))


def save_subgame(form):
    session = ORM.db()
    try:

        subgame = Subgame(
            game_id=form.id.data,
            name=form.name.data,
            url=form.url.data,
            img=form.img.data,
            createdAt=dt(),
            updatedAt=dt()
        )
        session.add(subgame)
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    return
