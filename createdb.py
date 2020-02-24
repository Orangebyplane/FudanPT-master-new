import _sqlite3

#运行程序前请先创建sqlite3数据库
connect=_sqlite3.connect('data_rank.db')
c=connect.cursor()
c.execute('CREATE TABLE student (number CHAR PRIMARY KEY,type integer ,grade integer )')
connect.commit()
connect.close()