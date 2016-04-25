class Resequencer:
    def __init__(self, plumber, params):
        self.plumber = plumber
        if "timeout" in params:
            self.timeout = params["timeout"]
        else:
            self.timeout = None
        if "count" in params:
            self.count = params["count"]
        else:
            self.count = None
        if "key_extractor" in params:
            self.key_extractor = params["key_extractor"]
        else:
            self.key_extractor = None
        if "reverse" in params:
            self.reverse = params["reverse"]
        else:
            self.reverse = False

    def resequence(self, exchanges):
        exchanges.sort(key=self.key_extractor, reverse=self.reverse)
