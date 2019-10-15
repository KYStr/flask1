# -*- coding: utf-8 -*-
from app.crud import crud
from flask import render_template, request, redirect, url_for
from app.models import Game, Subgame, Message, Menu
from app.orm import ORM


@crud.route("/read/one/", methods=("GET", "POST"))
def read_one():
    id = request.args.get("id", None)
    if id:
        data = dict(
            title="大賽詳情"
        )
        session = ORM.db()
        try:
            data['gam'] = session.query(Game).filter_by(id=int(id)).first()
            data['sub'] = session.query(Subgame).filter_by(
                game_id=int(id)).all()
            data['mes'] = session.query(Message).filter_by(
                game_id=int(id)).all()
            data['men'] = session.query(Menu).filter_by(
                game_id=int(id)).all()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return render_template("read_one.html", data=data)
    else:
        return redirect(url_for('crud.read_list'))
