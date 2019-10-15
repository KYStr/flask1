# -*- coding: utf-8 -*-
import mysql.connector  # 導入數據庫連接驅動
from sqlalchemy import create_engine  # 導入創建引擎工具
from sqlalchemy.orm import sessionmaker

mysql_configs = dict(
    db_host="127.0.0.1",
    db_name="crud",
    db_port=3306,
    db_user="root",
    db_pwd="q05qPO0nPeZrQ7J4"
)


class ORM(object):
    """docstring for  ORM"""
    @classmethod
    def db(cls):
        engine = create_engine(
            'mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'.format(
                **mysql_configs),
            encoding="utf-8",
            echo=False,
            pool_size=100,
            pool_recycle=10,
            connect_args={'charset': 'utf8'}
        )
        Session = sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=True,
            expire_on_commit=False,
        )
        return Session()

