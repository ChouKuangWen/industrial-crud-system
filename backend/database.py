from sqlalchemy import create_engine, text  # 建立資料庫連線引擎
from sqlalchemy.orm import sessionmaker, declarative_base  #產生DB session、建立 ORM 基底類別
from dotenv import load_dotenv
import os
load_dotenv()

# 定義連線資料庫的基本資訊
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_port = os.getenv("db_port")
db_name = os.getenv("db_name")

# mysql+pymysql://帳號:密碼@主機:埠號/資料庫?參數
db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?charset=utf8mb4"

# 建立資料庫連線引擎  建立 SessionLocal  宣告ORM
engine = create_engine(db_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ⚡ FastAPI Dependency：產生一個 DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
