##pseudo code
##very confused with many different api's and people not agreeing

class ApiRequests():
	def TextTransformation(dict):
		#trying to use text transformation's api
		insert into documents values (dict[Metadata][DOC ID], dict[Metadata][URL], 0, 0,
		  dict[Metadata][Title],
		  dict[Metadata][Descriptions],
		  dict[text][headings],
		  dict[Text][body]
		);
		for ngram in dict[grams]:
			insert into index values(ngram[gram],ngram[in_title],ngram[in_description],ngram[in_keywords],ngram[freq_headings],ngram[freq_text])


		
	def Crawling(dict):
		if(dict[operation] == "removed"):
			delete from documents where url = dict[url]
			##delete  from index

		if(dict[operation] == "moved"):
			update documents 
			set url = dict[url]
			where url = dict[url]

	def Ranking(dict):
		update documents
		set pagerank = dict[pagerank] ,  norm_pagerank = dict[norm_pagerank]
		where documents_pk = dict[url]


##	def Link(dict):

##//	def Query(dict):
