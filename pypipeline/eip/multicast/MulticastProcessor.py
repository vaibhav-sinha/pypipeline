from pypipeline.core.Processor import Processor
from pypipeline.util import ExchangeUtil

class MulticastProcessor(Processor):

    def __init__(self, multicast):
        super().__init__(None)
        self.multicast = multicast

    def _process(self, exchange):
        previous = None
        for pipeline in self.multicast.pipelines:
            to_send = ExchangeUtil.copy_exchange(exchange)
            pipeline.source.chain.process(to_send)
            previous = self.multicast.aggregator.aggregate(previous, to_send)
        if self.next is not None:
            self.next.process(previous)

