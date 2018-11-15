
class text_Transformation:

    def __init__(dict):
        self.meta_data = dict[Metadata]
        self.text = dict[text]
        self.grams = dict[grams]

    def toParam():
        return [self.meta_data, self.text, self.grams]

class link_Analysis():

    def __init__(dict):
        self.url = dict[url]
        self.page_rank = dict[pagerank]
        self.inlinks = dict[inlinks]

    def toParam():
        return [self.url, self.pagerank, self.inlinks]

class crawling():

    def __init___(dict):
        self.url = dict[url]
        self.old_url = dict[old_url]
        self.operation = dict[operation]

    def toParam():
        return [self.url, self.old_url, self.operation]
