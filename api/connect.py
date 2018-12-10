import psycopg2
from server_Objects import text_Transformation
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
                (query, parameter) = server_Object.insert_Doc(server_Object)
                cur.execute(query, parameter)
                id = cur.execute(
                    "SELECT id FROM documents WHERE url = '%s'", (server_Object.dict[metadata][url],))
                server_Object.addId(server_Object, id)
                print(id)

            # returns an array of tuples containing the query and parameters
            # server_Object=text_Transformation(dict)
            queries = server_Object.query(server_Object)

            for (query, parameters) in queries:
                # execute a stored procedure
                #print((query,parameters))
                cur.execute(query, parameters)
            conn.commit()

            # The PostgreSQL database server response
            # response = cur.fetchone()
            # print(response)
            # print(insert/update_Response)
            # print("HELLO")
            # Close the communication with the PostgreSQL
            cur.close()
            # print("CLOSED CUR")
            # return "It Works"
        except (Exception, psycopg2.DatabaseError) as error:
            # print("CAUGHT EXCEPTION")
            print("ERROR: ",error)
            return error
        finally:
            if conn is not None:
                conn.close()
                # print("CLOSE CONN")
        return 1

# if __name__ == '__main__':
#     connect()
