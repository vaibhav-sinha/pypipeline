import unittest
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core import EndpointRegistry
from pypipeline.core.Source import Source
from pypipeline.core.Destination import Destination
import inspect


class DslPipelineDefinitionBuilderTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        EndpointRegistry.add_endpoint("source1", Source1)
        EndpointRegistry.add_endpoint("to1", To1)
        EndpointRegistry.add_endpoint("to2", To2)

    def test_simple_pipeline(self):
        builder = DslPipelineBuilder()
        builder.source("source1://test?name=s1&type=abc").to("to1://t1").to("to2://t2")
        self.assertEqual(builder.source_class, Source1)

    def test_process_block(self):
        builder = DslPipelineBuilder()
        builder.source("source1://test?name=s1&type=abc").to("to1://t1").to("to2://t2").process(lambda x: print(x))
        self.assertEqual(builder.source_class, Source1)
        self.assertTrue(inspect.isclass(builder.to_list[2][0]))

    def test_one_source(self):
        builder = DslPipelineBuilder()
        with self.assertRaises(AssertionError):
            builder.to("to1://t1")

    def test_only_one_source(self):
        builder = DslPipelineBuilder()
        with self.assertRaises(AssertionError):
            builder.source("to1://t1").source("to1://t2")

    def test_build_pipeline(self):
        builder = DslPipelineBuilder()
        pipeline = builder.source("source1://test?name=s1").to("to1://t1").to("to2://t2").build()
        self.assertIsNotNone(pipeline.source.chain)

    def test_multicast_dsl(self):
        builder = DslPipelineBuilder()
        builder.source("source1://s1").to("to1://t1").multicast({})\
            .pipeline().to("to1://t11").to("to1://t12").end_pipeline()\
            .pipeline().to("to1://t21").to("to1://t22").end_pipeline()\
            .end_multicast().to("to1://t2")
        self.assertIsNotNone(builder.builder_stack[-1])


class Source1(Source):
    pass


class To1(Destination):
    pass


class To2(Destination):
    pass

if __name__ == '__main__':
    unittest.main()