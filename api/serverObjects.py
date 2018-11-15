class serverObject:

    def __init__(self, name):
        self.name = name
        
    def toParam(self):
        return [self]

class text_Transformation(serverObject):

    def __init__(self, dict):
        self.meta_data = dict[Metadata]
        self.text = dict[text]
        self.grams = dict[grams]

    def toParam(self):
        return [self.meta_data, self.text, self.grams]

class link_Analysis(serverObject):

    def __init__(self, dict):
        self.url = dict[url]
        self.page_rank = dict[pagerank]
        self.inlinks = dict[inlinks]

    def toParam(self):
        return [self.url, self.pagerank, self.inlinks]

class crawling(serverObject):

    def __init___(self, dict):
        self.url = dict[url]
        self.old_url = dict[old_url]
        self.operation = dict[operation]

    def toParam(self):
        return [self.url, self.old_url, self.operation]
