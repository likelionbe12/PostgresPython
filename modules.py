import psycopg2

class DB:
    def __init__(self, db_host, db_name, db_port, db_pwd, db_user):
        self.conn_params = {
                    'dbname': db_name,
                    'user': db_user,
                    'port' : db_port,
                    'password': db_pwd,
                    'host': db_host,
                }
        self.connect()
        
    def connect(self):
        self.conn = psycopg2.connect(**self.conn_params)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, query, args=None):
        self.cursor.execute(query, args)
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def insert(self, name, age):
        sql = "insert into users(name, age) values (%s, %s)"
        print(sql)
        self.cursor.execute(sql, [name, age])
        self.conn.commit()

    def read_datas(self):
        sql = "select * from users;"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print(rows)

    def read_data_with_condition(self, name):
        sql = "select * from users where name=%s;"
        self.cursor.execute(sql, (name,))
        rows = self.cursor.fetchall()
        return rows

    def update_data(self): # 나이를 수정
        # id 찾기
        target_name = input("수정할 데이터 이름을 입력 : ")
        sql_select = "select * from users where name=%s;"
        self.cursor.execute(sql_select, (target_name,))
        row = self.cursor.fetchone()
        target_id = row[0]
        # 수정 내용 적용
        update_age=input("수정할 나이를 입력하세요 : ")
        sql_update = "update users set age=%s where id=%s"
        self.cursor.execute(sql_update, (update_age,target_id))        

    def delete_data(self):
        target_name = input("지울 데이터 이름을 입력 : ")
        sql_delete = "delete from users where name=%s;"
        self.cursor.execute(sql_delete, (target_name,))
