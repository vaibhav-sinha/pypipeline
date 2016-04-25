from pypipeline.core.Destination import Destination


class Log(Destination):
    def process(self, exchange):
        print(exchange)