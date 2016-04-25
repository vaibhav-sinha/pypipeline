from pypipeline.core.Destination import Destination


class Log(Destination):
    def __init__(self, plumber, params):
        super().__init__(plumber, params)
        self.name = params["name"]

    def process(self, exchange):
        print("\nLog: " + self.name + "\n" + str(exchange) + "\n")