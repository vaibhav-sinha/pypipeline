class Source:
    def __init__(self, plumber, params):
        self.plumber = plumber
        self.chain = None
        self.params = params

    def start(self):
        raise NotImplementedError("Sources should implement their start method")

    def stop(self):
        raise NotImplementedError("Sources should implement their stop method")
