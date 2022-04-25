import psycopg2 
from psycopg2 import Error


try:
    connection = psycopg2.connect(user="xkdicbbn",password="qL3NUhqaIdLAwROTlnGeSpkNua4p3Oge",
    host = "raja.db.elephantsql.com", database="xkdicbbn")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sentiment_analysis")
    record = cursor.fetchone()
    print(record)
    
except(Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

# finally:
#     if(connection):
#         cursor.close()
