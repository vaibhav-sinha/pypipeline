import time
import unittest

from pypipeline.components.destination.Log import Log
from pypipeline.components.source.Timer import Timer
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Plumber import Plumber


class LogTest(unittest.TestCase):

    def test_log(self):
        plumber = Plumber()
        builder = DslPipelineBuilder()
        pipeline = builder.source(Timer, {"period": 1.0}).to(Log)
        plumber.add_pipeline(pipeline)
        plumber.start()
        time.sleep(1)
        plumber.stop()
