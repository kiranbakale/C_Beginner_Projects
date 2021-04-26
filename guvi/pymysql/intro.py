import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="karan@2000",
    database="sakila"
)

mycursor = mydb.cursor()
mycursor.execute("select * from actor")
myresult = mycursor.fetchone()

for x in myresult:
    print(x)
