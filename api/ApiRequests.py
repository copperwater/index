##pseudo code
##very confused with many different api's and people not agreeing
import psycopg2

class ApiRequests():

	try:
		## info  /home/rootc2/index, port = 5432
	    conn = psycopg2.connect("dbname='local' user='dbuser' host='localhost' password='dbpass'")
	except:
	    print "I am unable to connect to the database"
	    return False

	cur = conn.cursor()
	Metadata = "Metadata"
	DOCID = "DOC ID"
	url = "url"
	Text = "Text"
	headings ="headings"
	body = "body"
	operations = "operation"
	freq_headings = "freq_headings"
	freq_text = "freq_text"
	in_title = "in_title"
	norm_pagerank = "norm_pagerank"
	pagerank ="pagerank"

	def TextTransformation(dict):
		sql = """insert into documents values (%s, %s, 0, 0,
		  %s,
		  %s
		  %s,
		  %s)

		  """

		  sql2 = """
		  insert into index values(%s,%s,%s,%s,%s,%s)
		  """

		#trying to use text transformation's api
		curr.execute(sql,dict[Metadata][DOCID], dict[Metadata][url], 0, 0,
		  dict[Metadata][Title],
		  dict[Metadata][Descriptions],
		  dict[Text][headings],
		  dict[Text][body])

		for ngram in dict[grams]:
			curr.execute(sql2,ngram[gram],ngram[in_title],ngram[in_description],ngram[in_keywords],ngram[freq_headings],ngram[freq_text])


		
	def Crawling(dict):
		sql = """
		delete from documents where url = %s

		"""

		sql2 = """ update documents
		set url = %s
		where url = %s
		"""

		if(dict[operation] == "removed"):
			curr.execute(sql,dict[url])
			##delete  from index

		if(dict[operation] == "moved"):
			curr.execute(sql2,dict[url],dict[url])

	def Ranking(dict):
		sql = """
		update documents
		set pagerank = %s ,  norm_pagerank = %s
		where documents_pk = %s

		"""
		curr.execute(sql,dict[pagerank],dict[norm_pagerank],dict[url])


	def Link(dict):
		sql = """
		"""

##//	def Query(dict):
