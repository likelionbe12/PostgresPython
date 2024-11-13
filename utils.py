from dotenv import load_dotenv
import os

load_dotenv()

db_host=os.getenv("db_host")
db_port=os.getenv("db_port")
db_user=os.getenv("db_user")
db_pwd=os.getenv("db_pwd")
db_name=os.getenv("db_name")