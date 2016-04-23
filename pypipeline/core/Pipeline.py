from urllib.parse import parse_qs

from .Channel import Channel
from .Processor import Processor
from .Status import Status


class Pipeline:
    def __init__(self, builder, plumber=None):
        self.id = builder.id
        self.plumber = plumber
        self.status = Status.stopped
        self.auto_start = builder.auto_start
        source_params = parse_qs(builder.source_uri.query, True, True)
        self.source = builder.source_class(plumber, source_params)
        self.transient_previous = None
        for destination in builder.to_list:
            channel = Channel()
            if self.source.chain is None:
                self.source.chain = channel
            if destination[1] is not None:
                destination_params = parse_qs(destination[1].query)
            else:
                destination_params = {}
            destination_obj = destination[0](plumber, destination_params)
            processor = Processor(destination_obj)
            channel.next = processor
            if self.transient_previous is not None:
                self.transient_previous.next = channel
            self.transient_previous = processor

    def start(self):
        self.status = Status.starting
        self.source.start()
        self.status = Status.running

    def stop(self):
        self.status = Status.stopping
        self.source.stop()
        self.status = Status.stopped
