from pypipeline.core.Processor import Processor
import time


class AggregatorProcessor(Processor):

    def __init__(self, aggregator):
        super().__init__(None)
        self.aggregator = aggregator
        self.previous = None
        if "timeout" in aggregator.params:
            self.timeout = aggregator.params["timeout"]
            self.time = time.time()
        else:
            self.timeout = None

        if "count" in aggregator.params:
            self.count = aggregator.params["count"]
            self.current_count = 0
        else:
            self.count = None

        if self.count is None and self.timeout is None:
            raise ValueError("Atleast one of two terminating conditions must be specified: count, timeout")

    def _process(self, exchange):
        self.current_count += 1
        self.previous = self.aggregator.aggregate(self.previous, exchange)
        if self.count is not None and self.current_count == self.count:
            self.forward(self.previous)
            return
        if self.timeout is not None and time.time() - self.time >= self.timeout:
            self.forward(self.previous)
            return

    def forward(self, exchange):
        if self.next is not None:
            self.next.process(exchange)
        self.current_count = 0
        self.time = time.time()
        self.previous = None
