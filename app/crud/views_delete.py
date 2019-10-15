# -*- coding: utf-8 -*-
from app.crud import crud
from flask import request, redirect, url_for
from app.models import Game, Subgame, Message, Menu
from app.orm import ORM


@crud.route("/delete/", methods=("GET",))
def delete():
    id = request.args.get("id", None)
    if id:
        session = ORM.db()
        try:
            game = session.query(Game).filter_by(id=int(id)).first()
            subgame = session.query(Subgame).filter_by(game_id=int(id)).all()
            session.delete(game)
            for item in subgame:
                session.delete(item)
            message = session.query(Message).filter_by(game_id=int(id)).all()
            for item in message:
                session.delete(item)
            menu = session.query(Menu).filter_by(game_id=int(id)).all()
            for item in menu:
                session.delete(item)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
    return redirect(url_for('crud.read_list'))


@crud.route("/delete/message/", methods=("GET",))
def delete_message():
    id = request.args.get("id", None)
    game_id = request.args.get("game_id", None)
    if id and game_id:
        session = ORM.db()
        try:
            message = session.query(Message).filter_by(id=int(id)).first()
            session.delete(message)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
    return redirect(url_for('crud.read_one', id=game_id))


@crud.route("/delete/subgame/", methods=("GET",))
def delete_subgame():
    id = request.args.get("id", None)
    game_id = request.args.get("game_id", None)
    if id:
        session = ORM.db()
        try:
            subgame = session.query(Subgame).filter_by(id=int(id)).first()
            session.delete(subgame)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
    return redirect(url_for('crud.read_one', id=game_id))


@crud.route("/delete/menu/", methods=("GET",))
def delete_menu():
    id = request.args.get("id", None)
    game_id = request.args.get("game_id", None)
    if id:
        session = ORM.db()
        try:
            menu = session.query(Menu).filter_by(id=int(id)).first()
            session.delete(menu)
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
    return redirect(url_for('crud.read_one', id=game_id))
