import mysql.connector

db = mysql.connector.connect(user = "root", password = "KevinDuong2001@", host = "127.0.0.1", database = "BANK")
cursor = db.cursor()

code = """SELECT * FROM ADMIN_ACCOUNT;"""

cursor.execute(code)
data = cursor.fetchall()
print(data)