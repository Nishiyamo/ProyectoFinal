import mysql.connector
from mysql.connector import Error

def con():
    try:
        con = mysql.connector.connect(host='127.0.0.1',
                                            database='stocksdb',
                                            user='root',
                                            password='bunta')
        # cur = con.cursor(buffered=True)
        # cur.execute("select database()")
        # print(cur.fetchone()) 
    except Error as e:
        print("Error conectando a mysql: =>", e)

    return con
# con()