import time
import unittest

from pypipeline.components.source.Timer import Timer
from pypipeline.core.Destination import Destination
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder


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
