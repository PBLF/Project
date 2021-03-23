import cur as cur
import pymysql

con = pymysql.connect(host="localhost",user="root",password="Wyx134!#!$",database="Student",port=3306)
cur = con.cursor()

sql = "insert into Student.student(Id, Name, Age) values (%s,%s,%s)"


try:
    cur.execute(sql,("18006","伊索","18"))
    con.commit()
    print("插入数据成功")

except Exception as e:
    print(e)
    con.rollback()
    print("插入数据失败")

finally:
    cur.close()
