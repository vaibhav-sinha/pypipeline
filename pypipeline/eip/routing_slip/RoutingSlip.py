class RoutingSlip:
    def __init__(self, plumber, params):
        self.plumber = plumber
        self.params = params

    def slip(self, exchange):
        raise NotImplementedError("Subclass must implement the slip method")