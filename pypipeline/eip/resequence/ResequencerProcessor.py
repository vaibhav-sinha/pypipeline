from pypipeline.core.Processor import Processor
import time


class ResequencerProcessor(Processor):

    def __init__(self, resequencer):
        super().__init__(None)
        self.resequencer = resequencer
        self.exchanges = []
        if resequencer.timeout is not None:
            self.time = time.time()
        if resequencer.count is not None:
            self.current_count = 0

    def _process(self, exchange):
        self.exchanges.append(exchange)
        self.current_count += 1
        if self.resequencer.count is not None and self.current_count == self.resequencer.count:
            self.resequencer.resequence(self.exchanges)
            self.forward(self.exchanges)
            return
        if self.resequencer.timeout is not None and time.time() - self.time >= self.resequencer.timeout:
            self.resequencer.resequence(self.exchanges)
            self.forward(self.exchanges)
            return

    def forward(self, exchanges):
        if self.next is not None:
            for exchange in exchanges:
                self.next.process(exchange)
        self.current_count = 0
        self.time = time.time()
        self.previous = None
