class Processor:
    def __init__(self, obj):
        self.object = obj
        self.next = None

    def process(self, exchange):
        self.object.process(exchange)
        if self.next is not None:
            try:
                self.next.process(exchange)
            except Exception as e:
                raise e
