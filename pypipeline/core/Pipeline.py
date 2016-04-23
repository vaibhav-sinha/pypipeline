from urllib.parse import parse_qs

from .Channel import Channel
from .Processor import Processor
from .Status import Status
from .Destination import Destination
from pypipeline.eip.split.Splitter import Splitter
from pypipeline.eip.split.SplitterProcessor import SplitterProcessor
from pypipeline.eip.filter.Filter import Filter
from pypipeline.eip.filter.FilterProcessor import FilterProcessor


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
            if issubclass(destination[0], Destination):
                destination_obj = destination[0](plumber, destination_params)
                processor = Processor(destination_obj)
            if issubclass(destination[0], Splitter):
                destination_obj = destination[0]()
                processor = SplitterProcessor(destination_obj)
            if issubclass(destination[0], Filter):
                destination_obj = destination[0]()
                processor = FilterProcessor(destination_obj)
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
