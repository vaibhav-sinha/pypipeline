from urllib.parse import parse_qs
from.Channel import Channel
from.Processor import Processor


class Pipeline:
    def __init__(self, name, source_class, source_uri, to_list):
        self.id = name
        source_params = parse_qs(source_uri.query, True, True)
        self.source = source_class(source_params)
        self.transient_previous = None
        for destination in to_list:
            channel = Channel()
            channel_processor = Processor(channel)
            if self.source.chain is None:
                self.source.chain = channel_processor
            destination_params = parse_qs(destination[1])
            destination_obj = destination[0](destination_params)
            destination_processor = Processor(destination_obj)
            channel_processor.next = destination_processor
            if self.transient_previous is not None:
                self.transient_previous.next = channel_processor
