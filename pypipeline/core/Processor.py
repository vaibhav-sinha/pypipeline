class Processor:
    def __init__(self, obj):
        self.object = obj
        self.next = None

    def process(self, exchange):
        try:
            self._process(exchange)
        except Exception as e:
            raise e

    def _process(self, exchange):
        self.object.process(exchange)
        if self.next is not None:
            self.next.process(exchange)
