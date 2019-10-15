# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base  # 模型繼承父類
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, TINYINT, DATE, DATETIME, TEXT  # 導入數據類型
from sqlalchemy import Column  # 指定字段

Base = declarative_base()

"""
id			編號		BigInt 		primary-key
name		姓名		str			no null
job			職位		TinyInt		no null
sex			性別		TinyInt		no null
edu			學歷		TinyInt		no null
birth		生日		time		no null
email		郵箱		str			no null-only
phone		手機		str			no null-only
info		介紹		text		no null
face		頭像		str			no null
createdAt	添加時間	steap time	no null
updateAt	添加時間	steap time	no null
"""

class Employee(Base):
    __tablename__ = "employee"
    id = Column(BIGINT, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    job = Column(TINYINT, nullable=False)
    sex = Column(TINYINT, nullable=False)
    edu = Column(TINYINT, nullable=False)
    birth = Column(DATE, nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    phone = Column(VARCHAR(17), nullable=False, unique=True)
    info = Column(TEXT, nullable=False)
    face = Column(VARCHAR(100), nullable=False)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)



"""
id			編號		BigInt 		primery-key
employee_id	員工編號	BigInt		no null
hobby_key	愛好索引	TintInt		no null
createdAt	添加時間	steap time	no null
updateAt	添加時間	steap time	no null
"""
class Hobby(Base):
    __tablename__ = "hobby"
    id = Column(BIGINT, primary_key=True)
    employee_id = Column(BIGINT, nullable=False)
    hobby_key = Column(TINYINT, nullable=False)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)


"""
大賽數據模型
id          編號      BigInt      primary_key
name        大賽名稱    str         no null
email       郵箱      str         no null-only
createdAt   添加時間    steap time  no null
updateAt    添加時間    steap time  no null
"""
class Game(Base):
    __tablename__ = "game"
    id = Column(BIGINT, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)



"""
比賽數據模型
id          編號       BigInt      primary_key
game_id     大賽編號   BigInt      no null
name        比賽名稱   str         no null
url         比賽網址   str            no null
img         比賽圖片   str            no null
createdAt   添加時間   steap time  no null
updateAt    添加時間   steap time  no null
"""
class Subgame(Base):
    __tablename__ = "subgame"
    id = Column(BIGINT, primary_key=True)
    game_id = Column(BIGINT, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    url = Column(VARCHAR(255), nullable=False)
    img = Column(VARCHAR(100), nullable=False)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)


        
"""
公告數據模型
id          編號      BigInt      primary_key
game_id     大賽編號    BigInt      no null
title       公告標題    str         no null
content     公告內容 str            no null
createdAt   添加時間    steap time  no null
updateAt    添加時間    steap time  no null
"""
class Message(Base):
    __tablename__ = "message"
    id = Column(BIGINT, primary_key=True)
    game_id = Column(BIGINT, nullable=False)
    title = Column(VARCHAR(255), nullable=False)
    content = Column(VARCHAR(255), nullable=False)
    createdAt = Column(DATETIME, nullable=False)
    updatedAt = Column(DATETIME, nullable=False)


    
"""
菜單數據模型
id          編號      BigInt      primary_key
game_id     大賽編號    BigInt      no null
item        選項      str         no null
url         選項連結 str            no null
createdAt   添加時間    steap time  no null
"""
class Menu(Base):
    __tablename__ = "menu"
    id = Column(BIGINT, primary_key=True)
    game_id = Column(BIGINT, nullable=False)
    item = Column(VARCHAR(255), nullable=False)
    url = Column(VARCHAR(255), nullable=False)
    createdAt = Column(DATETIME, nullable=False)




if __name__ == "__main__":
    import mysql.connector  # 導入數據庫連接驅動
    from sqlalchemy import create_engine  # 導入創建引擎工具

    mysql_configs = dict(
        db_host="127.0.0.1",
        db_name="crud",
        db_port=3306,
        db_user="root",
        db_pwd="q05qPO0nPeZrQ7J4"
    )

    engine = create_engine(
        'mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8mb4'.format(
            **mysql_configs),
        encoding="utf-8",
        echo=True
    )

    metadata = Base.metadata
    metadata.create_all(engine)
    print("生成成功!")
