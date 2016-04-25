import unittest
from pypipeline.core.Plumber import Plumber
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Destination import Destination
from pypipeline.components.Timer import Timer
import time


class FilterTest(unittest.TestCase):

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        pipeline1 = builder1.source(Timer, {"period": 1.0}).routing_slip({"method": slip}).process(lambda ex: print(ex.in_msg.body))
        plumber.add_pipeline(pipeline1)
        plumber.start()
        time.sleep(1)
        plumber.stop()


def slip(exchange):
    return [
        (D1, {}),
        (D2, {})
    ]


class D1(Destination):
    def process(self, exchange):
        print(exchange.in_msg.body + " D1")


class D2(Destination):
    def process(self, exchange):
        print(exchange.in_msg.body + " D2")