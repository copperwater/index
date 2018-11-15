import psycopg2
from config import config

class connect():
    def insert(server_Object, stored_Procedure_Name):
        """ Connect to the PostgreSQL database server and Insert or Update Text Transformation"""
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            # print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            # execute a statement
            # print('PostgreSQL database version:')
            cur.execute(stored_Procedure_Name, text_Object)

            # display the PostgreSQL database server response
            insert/update_Response = cur.fetchone()
            print(insert/update_Response)

         # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

# if __name__ == '__main__':
#     connect()
