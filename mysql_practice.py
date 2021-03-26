import mysql.connector as mr
mydb = mr.connect(host='localhost',user='root',password='q1w2e3r4')
mycursor = mydb.cursor()
mycursor.execute('show databases')
for i in mycursor:
    print(i)