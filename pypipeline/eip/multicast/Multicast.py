from pypipeline.core.Source import Source


class Multicast(Source):
    def __init__(self, plumber, params):
        super().__init__(plumber, params)
        self.plumber = plumber
        self.params = params
