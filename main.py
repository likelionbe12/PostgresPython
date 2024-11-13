# DB접속정보 불러오기
# DB관리 Class
from utils import db_host, db_name, db_port, db_pwd, db_user
from modules import DB

# DB 객체를 만들기
db = DB(db_host, db_name, db_port, db_pwd, db_user)
# CRUD 실행
name = input("이름을 입력하세요 : ")
age = input("나이를 입력하세요 : ")
db.insert(name, age)
db.read_datas()
name = input("조회하고자 하는 이름을 입력하세요 : ")
db.read_data_with_condition(name) # 조회

# 업데이트
db.update_data()
# 업데이트 내용 확인
db.read_datas()

# 삭제
db.delete_data()
# 업데이트 내용 확인
db.read_datas()

# DB 연결 종료
db.close()

