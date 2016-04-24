class Aggregator:
    def __init__(self, plumber, params):
        self.plumber = plumber
        self.params = params

    def aggregate(self, old_exchange, current_exchange):
        return current_exchange
