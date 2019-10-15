# -*- coding: utf-8 -*-
from app.crud import crud
from flask import render_template, request
from app.models import Game, Subgame, Message, Menu
from app.orm import ORM

@crud.route("/game/", methods=("GET", "POST"))
def read_game():
    id = request.args.get("id", None)
    if id:
        session = ORM.db()
        data = dict()
        try:
            data['gam'] = session.query(Game).filter_by(id=int(id)).first()
            data['sub'] = session.query(Subgame).filter_by(
                game_id=int(id)).all()
            data['mes'] = session.query(Message).order_by(Message.updatedAt.desc()).filter_by(
                game_id=int(id)).all()
            data['men'] = session.query(Menu).filter_by(
                game_id=int(id)).all()
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return render_template("front.html", data=data)
    else:
        return 404
