class server_Object:

    def __init__(self, name):
        self.name = name

    def toParam(self):
        return [self]


class text_Transformation(server_Object):

    def __init__(self, dict):
        self.dict = dict
        self.meta_data = dict[Metadata]
        self.text = dict[text]
        self.grams = dict[grams]

    def addId(self, int id):
        self.id = id

    def insert_Doc(self):
        parameter = (self.dict[metadata][url],
                     self.dict[metadata][title],
                     self.dict[metadata][description],
                     self.dict[Text][headings],
                     self.dict[Text][body])
        query = "insert into documents (url, title, description, sect_headings, paragraphs) values (%s, %s,%s,%s,%s)"
        return arr = [(query, parameter)]

    def query(self):
        # generic query structure for TextTransformation
        for ngram_type, list_ngram_type in self.dict[ngrams][all]:
            if !list_ngram_type:
                continue
            # find the total number of occurences of 1ngrams, 2grams, 3grams, 4grams, and 5grmas
            # before we find frequency
            total_in_ngram_type = 0
            for ngram, occurence in list_ngram_type:
                total_in_ngram_type += occurence
            # header occurence of the ngram
            header_occurence = 0
            # total header occurences of the ngram type (ie. 1gram, 2gram,
            # etc...)
            total_header_in_ngram_type = 0
            for ngram, occurence in self.dict[ngrams][headers][ngram_type]:
                total_header_in_ngram_type += occurence
            # loop through the actual ngrams
            for ngram, occurence in list_ngram_type:
                # if the ngram is in the headers get the occurence
                if ngram in self.dict[ngrams][headers][ngram_type]:
                    header_occurence = self.dict[ngrams][headers][ngram_type].get(
                        ngram)
                parameters = (
                    ngram,
                    self.id,
                    ngram in self.dict[ngrams][title][ngram_type],
                    ngram in self.dict[Metadata][Descriptions],
                    ngram in self.dict[metadata][keywords],
                    float(header_occurence) /
                    total_header_in_ngram_type,
                    float(occurence) /
                    total_in_ngram_type)
                query1 = "insert into index (ngram, docid, in_title, in_desc, in_keywords, freq_headings, freq_text) values (%s,%s,%s,%s,%s,%s,%s)"
                arr.append((query1, parameters))
        return arr

    #unused function since query returns a list of tuples for (query, parameter)
    def toParam(self):
        return [self.meta_data, self.text, self.grams]


class link_Analysis(server_Object):

    def __init__(self, dict):
        self.url = dict[url]
        self.page_rank = dict[pagerank]
        self.inlinks = dict[inlinks]

    def query(self):
        # generic query structure for TextTransformation
        arr = []
        query = "update documents set pagerank = %s,  norm_pagerank = %s where url = %s"
        parameters = (
            self.dict[pagerank],
            self.dict[norm_pagerank],
            self.dict[url],
        )
        arr.append((query, parameters))
        return arr

    #unused function since query returns a list of tuples for (query, parameter)
    def toParam(self):
        return [self.url, self.pagerank, self.inlinks]


class crawling(server_Object):

    def __init___(self, dict):
        self.url = dict[url]
        self.old_url = dict[old_url]
        self.operation = dict[operation]

    def query(self):
        # generic query structure for TextTransformation
        arr = []
        query = "delete from documents where url = %s"
        arr.append((query, (self.dict[url],)))
        return arr

    #unused function since query returns a list of tuples for (query, parameter)
    def toParam(self):
        return [self.url, self.old_url, self.operation]
