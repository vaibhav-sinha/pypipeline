class Aggregator:
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

    def aggregate(self, old_exchange, current_exchange):
        return current_exchange
