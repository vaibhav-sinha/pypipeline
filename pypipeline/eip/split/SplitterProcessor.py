from pypipeline.core.Processor import Processor


class SplitterProcessor(Processor):

    def __init__(self, splitter):
        super().__init__(None)
        self.splitter = splitter

    def _process(self, exchange):
        exchanges = self.splitter.split(exchange)
        if self.next is not None:
            for ex in exchanges:
                self.next.process(ex)
