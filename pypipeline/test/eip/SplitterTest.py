import time
import unittest

from pypipeline.components.source.Timer import Timer
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Message import Message
from pypipeline.core.Plumber import Plumber


class SplitterTest(unittest.TestCase):

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        pipeline1 = builder1.source(Timer, {"period": 1.0}).split(split_method).process(lambda ex: print(ex.in_msg.body))
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
