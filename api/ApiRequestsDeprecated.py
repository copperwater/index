# pseudo code
# very confused with many different api's and people not agreeing
import psycopg2
import psycopg2.extras


# multiple functions that can be called to parse api Post requests and commit them to database
# Stored dict arguments as variables since i think we will change the values often
# might not work I could not test it

class ApiRequests():
    # try:
    # 	## info  /home/rootc2/index, port = 5432
    #     conn = psycopg2.connect("dbname='local' user='dbuser' host='localhost' password='dbpass'")
    # except:
    #     print("I am unable to connect to the database")
    # this fails right now add in corect information
    conn = psycopg2.connect(
        "dbname='template1' user='dbuser' host='localhost' password='dbpass'")
    cur = conn.cursor()
    Metadata = "Metadata"
    DOCID = "DOC ID"
    url = "url"
    Text = "Text"
    headings = "headings"
    body = "body"
    operations = "operation"
    freq_headings = "freq_headings"
    freq_text = "freq_text"
    in_title = "in_title"
    norm_pagerank = "norm_pagerank"
    pagerank = "pagerank"

    def TextTransformation(dict):
        sql = """insert into documents values (%s, %s, 0, 0,%s,%s,%s,%s)"""

        sql2 = """insert into index values(%s,%s,%s,%s,%s,%s)"""

        # trying to use text transformation's api
        try:
            curr.execute(sql, dict[Metadata][DOCID], dict[Metadata][url], 0, 0,
                         dict[Metadata][Title],
                         dict[Metadata][Descriptions],
                         dict[Text][headings],
                         dict[Text][body])
        except BaseException:
            print("error commiting to database")
            return False

        for ngram in dict[grams]:
            try:
                curr.execute(sql2, ngram[gram], ngram[in_title], ngram[in_description],
                             ngram[in_keywords], ngram[freq_headings], ngram[freq_text])
            except BaseException:
                print("error commiting to database")
                return False
        return False

    def Crawling(dict):
        sql = """delete from documents where url = %s"""

        sql2 = """ update documents
		set url = %s
		where url = %s"""

        if(dict[operation] == "removed"):
            try:
                curr.execute(sql, dict[url])
            except BaseException:
                print("error commiting to database")
                return False
            # delete  from index

        if(dict[operation] == "moved"):
            try:
                curr.execute(sql2, dict[url], dict[url])
            except BaseException:
                print("error commiting to database")
                return False

        return True

# still need checks if not indexed yet by TextTransformation
# also what is the difference between ranking and link analysis api?
    def Ranking(dict):
        sql = """update documents
		set pagerank = %s ,  norm_pagerank = %s
		where documents_pk = %s"""
        try:
            curr.execute(sql, dict[pagerank], dict[norm_pagerank], dict[url])
        except BaseException:
            print("error commiting to database")
            return False
        return True


# still need checks if not indexed yet by TextTransformation


    def Link(dict):
        sql = """update documents
		set pagerank = %s ,  norm_pagerank = %s
		where documents_pk = %s"""
        try:
            curr.execute(sql, dict[pagerank], dict[norm_pagerank], dict[url])
        except BaseException:
            print("error commiting to database")
            return False

        return True
# //	def Query(dict):
