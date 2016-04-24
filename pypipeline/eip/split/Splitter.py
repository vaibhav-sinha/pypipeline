class Splitter:
    def __init__(self, plumber):
        self.plumber = plumber

    def split(self, exchange):
        raise NotImplementedError("Derived classes should implement the split method")