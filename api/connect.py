import psycopg2
import serverObjects.py
from config import config

class connect():
    # serverObject is from TextTransformation, Crawling, or Link Analysis
    # stored_Procedure_Name is the name of the procedure that matches the server object being inserted
    def insert(server_Object, stored_Procedure_Name):
        """ Connect to the PostgreSQL database server and Insert or Update Text Transformation"""
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            # execute a stored procedure
            cur.callproc(stored_Procedure_Name, server_Object.toParam())

            # The PostgreSQL database server response
            insert/update_Response = cur.fetchone()
            # print(insert/update_Response)

            # Close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

# if __name__ == '__main__':
#     connect()
