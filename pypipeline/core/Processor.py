class Processor:
    def __init__(self, obj):
        self.object = obj
        self.next = None

    def process(self, exchange):
        self.object.process(exchange)
        self.next.process(exchange)