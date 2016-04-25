from pypipeline.core.Destination import Destination
from pypipeline.core.Processor import Processor
from pypipeline.core.Property import Property


class DynamicRouterProcessor(Processor):
    def __init__(self, dynamic_router):
        super().__init__(None)
        self.dynamic_router = dynamic_router

    def _process(self, exchange):
        endpoint = self.dynamic_router.route(exchange)
        while endpoint is not None:
            assert issubclass(endpoint[0], Destination)
            destination = endpoint[0](self.dynamic_router.plumber, endpoint[1])
            destination.process(exchange)
            exchange.properties[Property.slip_endpoint] = endpoint[0]
            endpoint = self.dynamic_router.route(exchange)
        if self.next is not None:
            self.next.process(exchange)