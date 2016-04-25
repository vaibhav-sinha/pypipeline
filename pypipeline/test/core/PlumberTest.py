import time
import unittest

from pypipeline.components.source.Timer import Timer
from pypipeline.core.Destination import Destination
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Plumber import Plumber


class PlumberTest(unittest.TestCase):

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        builder2 = DslPipelineBuilder()
        pipeline1 = builder1.source(Timer, {"period": 1.0}).to(MessageModifier).process(lambda ex: print(ex.in_msg.body + " Pipeline1"))
        pipeline2 = builder2.source(Timer, {"period": 2.0}).to(MessageModifier).process(lambda ex: print(ex.in_msg.body + " Pipeline2"))
        plumber.add_pipeline(pipeline1)
        plumber.add_pipeline(pipeline2)
        plumber.start()
        time.sleep(10)
        plumber.stop()


class MessageModifier(Destination):
    def process(self, exchange):
        exchange.in_msg.body += " modified"
