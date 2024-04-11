import mysql.connector  

try:
    mysql.connector.connect(
        user="root",
        password = "blueberry123",
        host = "localhost",
        port = 2323,
        name = "student"
    )

except :
    print("cannot connect")
