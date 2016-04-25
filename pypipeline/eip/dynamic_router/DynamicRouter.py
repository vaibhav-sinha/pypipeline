class DynamicRouter:
    def __init__(self, plumber, params):
        self.plumber = plumber
        self.params = params

    def route(self, exchange):
        raise NotImplementedError("Subclass must implement the route method")