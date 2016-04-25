class Validator:
    def __init__(self, plumber):
        self.plumber = plumber

    def validate(self, exchange):
        raise NotImplementedError("Derived classes should implement the filter method")