from pypipeline.core.Destination import Destination
from pypipeline.util import ExchangeUtil


class Channel:
    def __init__(self, plumber, params):
        self.next = None
        self.plumber = plumber
        if "wiretap" in params and params["wiretap"] is not None:
            assert issubclass(params["wiretap"][0], Destination)
            self.wiretap = params["wiretap"][0](self.plumber, params["wiretap"][1])
        else:
            self.wiretap = None

    def process(self, exchange):
        try:
            if self.wiretap is not None:
                exchange_copy = ExchangeUtil.copy_exchange(exchange)
                self.wiretap.process(exchange_copy)
            self.next.process(exchange)
        except Exception as e:
            raise e
