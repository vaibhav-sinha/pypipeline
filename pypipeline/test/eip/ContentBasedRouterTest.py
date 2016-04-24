import unittest
from pypipeline.core.Plumber import Plumber
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.components.Timer import Timer
import time


class ContentBasedRouterTest(unittest.TestCase):

    def test_simple_pipeline(self):
        plumber = Plumber()
        builder1 = DslPipelineBuilder()
        pipeline1 = builder1.source(Timer, {"period": 1.0}).content_based_router() \
            .when(lambda ex: int(ex.in_msg.body.split()[-1]) % 3 == 0).pipeline().process(lambda ex: print(ex.in_msg.body + " %0")).end_pipeline() \
            .when(lambda ex: int(ex.in_msg.body.split()[-1]) % 3 == 1).pipeline().process(lambda ex: print(ex.in_msg.body + " %1")).end_pipeline() \
            .otherwise().pipeline().process(lambda ex: print(ex.in_msg.body + " Otherwise")).end_pipeline() \
            .end_content_based_router().process(lambda ex: print(ex.in_msg.body + " Last"))
        plumber.add_pipeline(pipeline1)
        plumber.start()
        time.sleep(10)
        plumber.stop()

