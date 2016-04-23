class Channel:
    def __init__(self):
        self.next = None

    def process(self, exchange):
        try:
            self.next.process(exchange)
        except Exception as e:
            raise e
