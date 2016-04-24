from pypipeline.core.Processor import Processor
import copy
import uuid


class MulticastProcessor(Processor):

    def __init__(self, multicast):
        super().__init__(None)
        self.multicast = multicast

    def _process(self, exchange):
        previous = None
        for pipeline in self.multicast.pipelines:
            to_send = self.copy_exchange(exchange)
            pipeline.source.chain.process(to_send)
            previous = self.multicast.aggregator.aggregate(previous, to_send)
        if self.next is not None:
            self.next.process(previous)

    def copy_exchange(self, ex):
        exchange = copy.copy(ex)
        exchange.id = uuid.uuid4()
        exchange.in_msg = copy.deepcopy(ex.in_msg)
        exchange.out_msg = copy.deepcopy(ex.out_msg)
        exchange.properties = copy.deepcopy(ex.properties)
        return exchange
