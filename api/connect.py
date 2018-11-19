import psycopg2
import serverObjects.py
from config import config

class connect():
    # serverObject is from TextTransformation, Crawling, or Link Analysis
    def insert(server_Object):
        """ Connect to the PostgreSQL database server and Insert or Update Text Transformation"""
        conn = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()
            # returns an array of tuples containing the query and parameters
            queries = serverObject.query()

            for (query, parameters) in queries:
                # execute a stored procedure
                cur.execute(query, parameters)

            # The PostgreSQL database server response
            response = cur.fetchone()
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
