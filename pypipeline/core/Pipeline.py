from urllib.parse import parse_qs

from .Channel import Channel
from .Processor import Processor
from .Status import Status
from .Destination import Destination
from pypipeline.eip.split.Splitter import Splitter
from pypipeline.eip.split.SplitterProcessor import SplitterProcessor
from pypipeline.eip.filter.Filter import Filter
from pypipeline.eip.filter.FilterProcessor import FilterProcessor
from pypipeline.eip.multicast.Multicast import Multicast
from pypipeline.eip.multicast.MulticastProcessor import MulticastProcessor


class Pipeline:
    def __init__(self, builder, plumber):
        self.id = builder.id
        self.plumber = plumber
        self.status = Status.stopped
        self.auto_start = builder.auto_start
        source_params = parse_qs(builder.source_uri.query, True, False)
        self.source = builder.source_class(plumber, source_params)
        self.transient_previous = None
        for destination in builder.to_list:
            channel = Channel()
            if self.source.chain is None:
                self.source.chain = channel
            if issubclass(destination[0], Destination):
                if destination[1] is not None:
                    destination_params = parse_qs(destination[1].query)
                else:
                    destination_params = {}
                destination_obj = destination[0](plumber, destination_params)
                processor = Processor(destination_obj)
            if issubclass(destination[0], Splitter):
                destination_obj = destination[0](plumber)
                processor = SplitterProcessor(destination_obj)
            if issubclass(destination[0], Filter):
                destination_obj = destination[0](plumber)
                processor = FilterProcessor(destination_obj)
            if destination[0] == Multicast:
                destination_obj = destination[0](plumber, destination[1])
                processor = MulticastProcessor(destination_obj)
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
