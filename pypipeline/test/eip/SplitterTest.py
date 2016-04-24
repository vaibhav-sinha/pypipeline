import unittest
from pypipeline.core.Plumber import Plumber
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Message import Message
from pypipeline.components.Timer import Timer
import time


class SplitterTest(unittest.TestCase):

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        pipeline1 = builder1.source({"endpoint": Timer, "period": 1.0}).split(split_method).process(lambda ex: print(ex.in_msg.body))
        plumber.add_pipeline(pipeline1)
        plumber.start()
        time.sleep(1)
        plumber.stop()


def split_method(exchange):
    exchanges = []
    for s in exchange.in_msg.body.split():
        ex = exchange.plumber.create_exchange()
        ex.in_msg = Message()
        ex.in_msg.body = s
        exchanges.append(ex)
    return exchanges
