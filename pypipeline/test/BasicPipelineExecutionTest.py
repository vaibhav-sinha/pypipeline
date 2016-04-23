import unittest
from pypipeline.core import EndpointRegistry
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Destination import Destination
from pypipeline.components.Timer import Timer
import time


class BasicPipelineExecutionTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        EndpointRegistry.add_endpoint("timer", Timer)
        EndpointRegistry.add_endpoint("mm", MessageModifier)

    def test_simple_pipeline(self):
        builder = DslPipelineBuilder()
        pipeline = builder.source("timer://test?period=2.0").to("mm://test").process(lambda ex: print(ex.in_msg.body)).build()
        pipeline.start()
        time.sleep(10)
        pipeline.stop()


class MessageModifier(Destination):
    def process(self, exchange):
        exchange.in_msg.body += " modified"
