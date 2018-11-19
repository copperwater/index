class serverObject:

    def __init__(self, name):
        self.name = name

    def toParam(self):
        return [self]

class text_Transformation(serverObject):

    def __init__(self, dict):
        self.dict = dict
        self.meta_data = dict[Metadata]
        self.text = dict[text]
        self.grams = dict[grams]

    def query(self):
        # generic query structure for TextTransformation
        parameter = (self.dict[Metadata][DOCID], self.dict[Metadata][url],
          self.dict[Metadata][Title],
          self.dict[Metadata][Descriptions],
          self.dict[Text][headings],
          self.dict[Text][body])
        query = "insert into documents (id, url, title, description, sect_headings, paragraphs) values (%s, %s, %s,%s,%s,%s)"
        return_dict = {query:parameter}
        for ngram in self.dict[grams]
            parameter =
            query = "insert into index values(%s,%s,%s,%s,%s,%s)"
        return

    def toParam(self):
        return [self.meta_data, self.text, self.grams]

class link_Analysis(serverObject):

    def __init__(self, dict):
        self.url = dict[url]
        self.page_rank = dict[pagerank]
        self.inlinks = dict[inlinks]

    def query():
        # generic query structure for TextTransformation
        return ""

    def toParam(self):
        return [self.url, self.pagerank, self.inlinks]

class crawling(serverObject):

    def __init___(self, dict):
        self.url = dict[url]
        self.old_url = dict[old_url]
        self.operation = dict[operation]

    def query():
        # generic query structure for TextTransformation
        return ""

    def toParam(self):
        return [self.url, self.old_url, self.operation]
