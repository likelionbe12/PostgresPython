# DB접속정보 불러오기
# DB관리 Class
from utils import db_host, db_name, db_port, db_pwd, db_user
from modules import DB

# DB 객체를 만들기
db = DB(db_host, db_name, db_port, db_pwd, db_user)
# CRUD 실행