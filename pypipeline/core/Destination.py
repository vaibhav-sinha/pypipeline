class Destination:
    def __init__(self, plumber, params):
        self.plumber = plumber
        self.params = params

    def process(self, exchange):
        raise NotImplementedError("Subclass of destination needs to implement process method")
