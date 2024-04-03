import mysql.connector

conn = mysql.connector.connect(
    user="root",
    password="",
    host="127.0.0.1",
    database="fastapi_demo"
)

# 2 tech to db : 1. Query builder, 2. ORM
sql = "SELECT * FROM employee"
cursor = conn.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    # print(row)
    print(row[1])
cursor.close()
conn.close()