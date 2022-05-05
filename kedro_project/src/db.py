import psycopg2 
from psycopg2 import Error


def db_connection(sentiment):
    connection = None
    try:
        connection = psycopg2.connect(user="ttlabs",password="sentimentanalysis",
        host = "database-sentimentanalysis.cslen5ruirkd.us-east-1.rds.amazonaws.com",database="postgres", port= 5432)    
        cursor = connection.cursor()
        cursor.execute("select * from sentiment_analysis  where sentiment_request_type = '{}'".format(sentiment))
        record = cursor.fetchall()
    except(Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    return record