from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import mysql.connector
from sqlalchemy.orm import declarative_base,sessionmaker



e =create_engine( "sqlite:///students.db")
Session=sessionmaker(bind=e)
s=Session()
met=MetaData()

base=declarative_base()

class students(base):
    __tablename__='students'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)

output=s.query(students) 
for line in  output:
    print(line.name)
  



