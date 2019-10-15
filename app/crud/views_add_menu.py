from app.crud import crud
from flask import render_template, request, jsonify, redirect
from app.forms import MenuAddForm
from app.orm import ORM
from app.models import Game, Menu
from app.crud.views_common import dt, get_gam


@crud.route("/add/menu/", methods=("GET", "POST"))
def add_menu():
    id = request.args.get("id", None)

    data = dict(
        title="新增連結"
    )
    if request.method == "POST":
        res = dict(code=0)
        form = MenuAddForm()
        if form.validate():
            save_menu(form)
            res['code'] = 1
        else:
            res = form.errors
            res["code"] = 0
        return jsonify(res)
    else:
        if id:
            data["gam"] = get_gam(id)
            return render_template("add_menu.html", data=data)
        else:
            return redirect(url_for('crud.read_one', id=id))



def save_menu(form):
    session = ORM.db()
    try:
        menu = Menu(
            game_id=form.id.data,
            item=form.name.data,
            url=form.url.data,
            createdAt=dt()
        )
        session.add(menu)
    except Exception as e:
        session.rollback()
    else:
        session.commit()
    finally:
        session.close()
    return
