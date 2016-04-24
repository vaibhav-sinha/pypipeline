import unittest
from pypipeline.core.Plumber import Plumber
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.components.Timer import Timer
import time


class MulticastTest(unittest.TestCase):

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        pipeline1 = builder1.source(Timer, {"period": 1.0}).multicast({"aggregate_method": aggregate}) \
            .pipeline().process(lambda ex: print(ex.in_msg.body + " P11")).process(to_upper).process(lambda ex: print(ex.in_msg.body + " P12")).end_pipeline() \
            .pipeline().process(lambda ex: print(ex.in_msg.body + " P21")).end_pipeline() \
            .end_multicast().process(lambda ex: print(ex.in_msg.body + " Last"))
        plumber.add_pipeline(pipeline1)
        plumber.start()
        time.sleep(10)
        plumber.stop()


def to_upper(exchange):
    exchange.in_msg.body = exchange.in_msg.body.upper()


def aggregate(old_exchange, current_exchange):
    if old_exchange is not None:
        current_exchange.in_msg.body += old_exchange.in_msg.body
    return current_exchange
