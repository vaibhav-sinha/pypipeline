import unittest
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Destination import Destination
from pypipeline.components.Timer import Timer
import time


class BasicPipelineExecutionTest(unittest.TestCase):

    def test_simple_pipeline(self):
        builder = DslPipelineBuilder()
        pipeline = builder.source(Timer, {"period": 2.0}).to(MessageModifier).process(lambda ex: print(ex.in_msg.body)).build()
        pipeline.start()
        time.sleep(10)
        pipeline.stop()


class MessageModifier(Destination):
    def process(self, exchange):
        exchange.in_msg.body += " modified"
