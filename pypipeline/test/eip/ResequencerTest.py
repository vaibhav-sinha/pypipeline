import random
import time
import unittest

from pypipeline.components.source.Timer import Timer
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Plumber import Plumber


class ResequencerTest(unittest.TestCase):

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        pipeline1 = builder1.source(Timer, {"period": 1.0}).process(insert_seq_number).resequencer({"key_extractor": get_key, "count": 5, "reverse": True}).process(lambda ex: print(ex.in_msg.headers["seq_num"]))
        plumber.add_pipeline(pipeline1)
        plumber.start()
        time.sleep(12)
        plumber.stop()


def insert_seq_number(exchange):
    exchange.in_msg.headers["seq_num"] = random.randint(0, 100)


def get_key(ex):
    return ex.in_msg.headers["seq_num"]