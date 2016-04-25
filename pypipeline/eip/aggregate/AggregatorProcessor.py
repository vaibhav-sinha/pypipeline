from pypipeline.core.Processor import Processor
import time


class AggregatorProcessor(Processor):

    def __init__(self, aggregator):
        super().__init__(None)
        self.aggregator = aggregator
        self.previous = None
        if aggregator.timeout is not None:
            self.time = time.time()
        if aggregator.count is not None:
            self.current_count = 0

    def _process(self, exchange):
        self.current_count += 1
        self.previous = self.aggregator.aggregate(self.previous, exchange)
        if self.aggregator.count is not None and self.current_count == self.aggregator.count:
            self.forward(self.previous)
            return
        if self.aggregator.timeout is not None and time.time() - self.time >= self.aggregator.timeout:
            self.forward(self.previous)
            return

    def forward(self, exchange):
        if self.next is not None:
            self.next.process(exchange)
        self.current_count = 0
        self.time = time.time()
        self.previous = None
