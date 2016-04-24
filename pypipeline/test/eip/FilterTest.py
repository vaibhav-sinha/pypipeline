import unittest
from pypipeline.core.Plumber import Plumber
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.components.Timer import Timer
import time


class FilterTest(unittest.TestCase):

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        pipeline1 = builder1.source(Timer, {"period": 1.0}).filter(Filter()).process(lambda ex: print(ex.in_msg.body))
        plumber.add_pipeline(pipeline1)
        plumber.start()
        time.sleep(10)
        plumber.stop()


class Filter:
    def __call__(self, exchange):
        parts = exchange.in_msg.body.split()
        return int(parts[-1]) % 2 == 0


def filter_method(exchange):
    parts = exchange.in_msg.body.split()
    return int(parts[-1]) % 2 == 0
