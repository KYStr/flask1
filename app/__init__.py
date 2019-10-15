# -*- coding: utf-8 -*-
from flask import Flask
from flask_wtf import CSRFProtect

#開啟表單令牌,防止跨站偽裝登陸、請求
csrf = CSRFProtect()

def create_app():
	app = Flask(__name__) #實例化
	app.config.from_object("app.configs")
	csrf.init_app(app)
	from app.crud import crud
	app.register_blueprint(crud)
	return app


