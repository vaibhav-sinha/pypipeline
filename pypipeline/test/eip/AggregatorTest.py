import unittest
from pypipeline.core import EndpointRegistry
from pypipeline.core.Plumber import Plumber
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.components.Timer import Timer
import time


class AggregatorTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        EndpointRegistry.add_endpoint("timer", Timer)

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        pipeline1 = builder1.source("timer://test?period=1.0").aggregate({"method": aggregate, "count": 5, "timeout": 2}).process(lambda ex: print(ex.in_msg.body))
        plumber.add_pipeline(pipeline1)
        plumber.start()
        time.sleep(12)
        plumber.stop()


def to_upper(exchange):
    exchange.in_msg.body = exchange.in_msg.body.upper()


def aggregate(old_exchange, current_exchange):
    if old_exchange is not None:
        current_exchange.in_msg.body += old_exchange.in_msg.body
    return current_exchange