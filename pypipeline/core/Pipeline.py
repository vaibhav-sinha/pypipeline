from urllib.parse import parse_qs

from .Channel import Channel
from .Processor import Processor


class Pipeline:
    def __init__(self, name, source_class, source_uri, to_list):
        self.id = name
        source_params = parse_qs(source_uri.query, True, True)
        self.source = source_class(source_params)
        self.transient_previous = None
        for destination in to_list:
            channel = Channel()
            if self.source.chain is None:
                self.source.chain = channel
            if destination[1] is not None:
                destination_params = parse_qs(destination[1].query)
            else:
                destination_params = {}
            destination_obj = destination[0](destination_params)
            processor = Processor(destination_obj)
            channel.next = processor
            if self.transient_previous is not None:
                self.transient_previous.next = channel
            self.transient_previous = processor

    def start(self):
        self.source.start()

    def stop(self):
        self.source.stop()
