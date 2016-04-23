from pypipeline.core.Processor import Processor


class FilterProcessor(Processor):

    def __init__(self, filter):
        super().__init__(None)
        self.filter = filter

    def _process(self, exchange):
        result = self.filter.filter(exchange)
        if result and self.next is not None:
            self.next.process(exchange)
