import mysql.connector
from dotenv import load_dotenv
import os

def ConnectorMysql():
    load_dotenv()
    database_name = os.getenv('DATABASE_NAME')
    database_host = os.getenv('DATABASE_HOST')
    database_port = str(os.getenv('DATABASE_PORT'))
    print(database_name)
    print(database_host)
    print(database_port)
    mydb = mysql.connector.connect(
            host=database_host,
            port=int(database_port),
            user="root",
            password="12345678",
            database=database_name,
    )
    return mydb

def create_table():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL
    );
    """
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("Table 'user' created successfully (if not already present).")

def list_data():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM user"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    data = []
    if len(myresult) > 0: 
        for x in myresult:
            arr = {
                "_id" : x[0],
                "name" : x[1],
                "age" : int(x[2]),
                }
            data.append(arr)
    return data

def get_data(_id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM user WHERE id='{}'; ".format(_id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) > 0: 
        for x in myresult:
            arr = {
                "_id" : x[0],
                "name" : x[1],
                "age" : int(x[2]),
                }
    return arr

def insert_data(name, age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (name,age) VALUES (%s ,%s)"
    val = (name, age)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    

def update_data(_id, name, age):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "UPDATE user SET  name=%s , age=%s WHERE id=%s"
    val = (name, age, _id)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.close()
    mydb.close()


def delete_data(_id):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = "DELETE  FROM user WHERE id={}".format(_id)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()