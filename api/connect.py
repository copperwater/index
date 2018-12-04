import psycopg2
import server_Objects
from config import config


class connect():
    # server_Object is from TextTransformation, Crawling, or Link Analysis
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
            # adds the docid correctly so we can use it for text transformations
            # insert of ngrams
            if isinstance(server_Object, text_Transformation):
                (query, parameter) = server_Object.insert_Doc()
                cur.execute(query, parameter)
                id = cur.execute(
                    "SELECT id FROM documents WHERE url = %s", (server_Object.dict[metadata][url],))
                server_Object.addId(id)

            # returns an array of tuples containing the query and parameters
            queries = server_Object.query()

            for (query, parameters) in queries:
                # execute a stored procedure
                cur.execute(query, parameters)

            # The PostgreSQL database server response
            response = cur.fetchone()
            # print(insert/update_Response)

            # Close the communication with the PostgreSQL
            cur.close()
            return "It Works"
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()

# if __name__ == '__main__':
#     connect()
