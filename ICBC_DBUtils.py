import pymysql

host = "localhost"
user = "root"
password = "root"
database = "bank"

def update(sql, param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    curson = con.cursor()
    curson.execute(sql, param)
    con.commit()
    curson.close()
    con.close()

def select(sql, param, mode = "all", size = 1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    curson = con.cursor()
    curson.execute(sql, param)
    if mode == 'all':
        return curson.fetchall()
    elif mode == 'one':
        return curson.fetchone()
    elif mode == 'many':
        return curson.fetchmany(size)
    con.commit()
    curson.close()
    con.close()