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
from pypipeline.eip.aggregate.Aggregator import Aggregator
from pypipeline.eip.aggregate.AggregatorProcessor import AggregatorProcessor
from pypipeline.eip.cbr.ContentBasedRouter import ContentBasedRouter
from pypipeline.eip.cbr.ContentBasedRouterProcessor import ContentBasedRouterProcessor
from pypipeline.eip.routing_slip.RoutingSlip import RoutingSlip
from pypipeline.eip.routing_slip.RoutingSlipProcessor import RoutingSlipProcessor
from pypipeline.eip.dynamic_router.DynamicRouter import DynamicRouter
from pypipeline.eip.dynamic_router.DynamicRouterProcessor import DynamicRouterProcessor
from pypipeline.eip.resequence.Resequencer import Resequencer
from pypipeline.eip.resequence.ResequencerProcessor import ResequencerProcessor
from pypipeline.eip.validate.Validator import Validator
from pypipeline.eip.validate.ValidatorProcessor import ValidatorProcessor


class Pipeline:
    def __init__(self, builder, plumber):
        self.id = builder.id
        self.plumber = plumber
        self.status = Status.stopped
        self.auto_start = builder.auto_start
        self.source = builder.source_class(plumber, builder.source_params)
        self.transient_previous = None
        for destination in builder.to_list:
            channel = Channel()
            if self.source.chain is None:
                self.source.chain = channel
            if issubclass(destination[0], Destination):
                destination_obj = destination[0](plumber, destination[1])
                processor = Processor(destination_obj)
            if issubclass(destination[0], Splitter):
                destination_obj = destination[0](plumber)
                processor = SplitterProcessor(destination_obj)
            if issubclass(destination[0], Filter):
                destination_obj = destination[0](plumber)
                processor = FilterProcessor(destination_obj)
            if issubclass(destination[0], Aggregator):
                destination_obj = destination[0](plumber, destination[1])
                processor = AggregatorProcessor(destination_obj)
            if issubclass(destination[0], RoutingSlip):
                destination_obj = destination[0](plumber, destination[1])
                processor = RoutingSlipProcessor(destination_obj)
            if issubclass(destination[0], DynamicRouter):
                destination_obj = destination[0](plumber, destination[1])
                processor = DynamicRouterProcessor(destination_obj)
            if issubclass(destination[0], Validator):
                destination_obj = destination[0](plumber)
                processor = ValidatorProcessor(destination_obj)
            if destination[0] == Multicast:
                destination_obj = destination[0](plumber, destination[1])
                processor = MulticastProcessor(destination_obj)
            if destination[0] == ContentBasedRouter:
                destination_obj = destination[0](plumber, destination[1])
                processor = ContentBasedRouterProcessor(destination_obj)
            if destination[0] == Resequencer:
                destination_obj = destination[0](plumber, destination[1])
                processor = ResequencerProcessor(destination_obj)
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
