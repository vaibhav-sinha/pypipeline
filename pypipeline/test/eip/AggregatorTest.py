import time
import unittest

from pypipeline.components.source.Timer import Timer
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Plumber import Plumber


class AggregatorTest(unittest.TestCase):

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        pipeline1 = builder1.source(Timer, {"period": 1.0}).aggregate({"method": aggregate, "count": 5, "timeout": 2}).process(lambda ex: print(ex.in_msg.body))
        plumber.add_pipeline(pipeline1)
        plumber.start()
        time.sleep(12)
        plumber.stop()


def aggregate(old_exchange, current_exchange):
    if old_exchange is not None:
        current_exchange.in_msg.body += old_exchange.in_msg.body
    return current_exchange
