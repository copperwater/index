class server_Object:

    def __init__(self, name):
        self.name = name

    def toParam(self):
        return [self]


class text_Transformation(server_Object):

    def __init__(self, dict):
        self.dict = dict
        self.meta_data = dict["metadata"]
        #self.text = dict[text]
        self.id = 1
        self.grams = dict["ngrams"]

    def addId(self, id):
        self.id = id

    def insert_Doc(self):
        # commented out changes since there is no text field in text transformation
        # parameter = (self.dict["metadata"]["url"],
        #              self.dict["metadata"][title],
        #              self.dict["metadata"][description],
        #              self.dict[text][headings],
        #              self.dict[text][body])
        parameter = (self.dict["metadata"]["url"],
                     self.dict["metadata"]["title"],
                     self.dict["metadata"]["description"])
        # query = "insert into documents ("url", title, description,
        # sect_headings, paragraphs) values (%s, %s,%s,%s,%s)"
        query = "insert into documents (url, title, description) values (%s, %s,%s)"
        return [(query, parameter)]

    def query(self):
        arr = []
        # generic query structure for TextTransformation
        for ngram_type in self.dict["ngrams"]["all"]:
            if not self.dict["ngrams"]["all"][ngram_type]:
                continue
            # find the total number of occurences of 1ngrams, 2grams, 3grams, 4grams, and 5grmas
            # before we find frequency
            total_in_ngram_type = 0
            for ngram in self.dict["ngrams"]["all"][ngram_type]:
                total_in_ngram_type += self.dict["ngrams"]["all"][ngram_type][ngram]
            # header occurence of the ngram
            header_occurence = 0
            # total header occurences of the ngram type (ie. 1gram, 2gram,
            # etc...)
            total_header_in_ngram_type = 0
            for ngram in self.dict["ngrams"]["headers"][ngram_type]:
                total_header_in_ngram_type += self.dict["ngrams"]["headers"][ngram_type][ngram]
            # loop through the actual ngrams
            for ngram in self.dict["ngrams"]["all"][ngram_type]:
                # if the ngram is in the headers get the occurence
                if ngram in self.dict["ngrams"]["headers"][ngram_type]:
                    header_occurence = self.dict["ngrams"]["headers"][ngram_type][ngram]
                parameters = (
                    ngram,
                    self.id,
                    ngram in self.dict["ngrams"]["title"][ngram_type],
                    ngram in self.dict["metadata"]["description"],
                    ngram in self.dict["metadata"]["keywords"],
                    float(header_occurence) /
                    total_header_in_ngram_type,
                    float(self.dict["ngrams"]["all"][ngram_type][ngram]) /
                    total_in_ngram_type)
                query1 = "insert into index (ngram, docid, in_title, in_desc, in_keywords, freq_headings, freq_text) values (%s,%s,%s,%s,%s,%s,%s)"
                arr.append((query1, parameters))
        return arr

    # unused function since query returns a list of tuples for (query,
    # parameter)
    def toParam(self):
        return [self.meta_data, self.text, self.grams]


class link_Analysis(server_Object):

    def __init__(self, dict):
        self.url = dict["url"]
        self.page_rank = dict[pagerank]
        self.norm_pagerank = dict[norm_pagerank]

    def query(self):
        # generic query structure for TextTransformation
        arr = []
        query = "update documents set pagerank = %s,  norm_pagerank = %s where url = %s"
        parameters = (
            self.dict[pagerank],
            self.dict[norm_pagerank],
            self.dict["url"],
        )
        arr.append((query, parameters))
        return arr

    # unused function since query returns a list of tuples for (query,
    # parameter)
    def toParam(self):
        return [self.url, self.pagerank, self.inlinks]


class crawling(server_Object):

    def __init___(self, dict):
        # we dont know the name for this
        self.url = dict["urls"]

    def query(self):
        # generic query structure for TextTransformation
        arr = []
        for link in self.url:
            query = "delete from documents where url = %s"
            arr.append((query, (link,)))
        return arr

    # unused function since query returns a list of tuples for (query,
    # parameter)
    def toParam(self):
        return [self.url, self.old_url, self.operation]
