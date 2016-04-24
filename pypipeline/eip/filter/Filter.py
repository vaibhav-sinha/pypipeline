class Filter:
    def __init__(self, plumber):
        self.plumber = plumber

    def filter(self, exchange):
        raise NotImplementedError("Derived classes should implement the filter method")