import unittest
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core import EndpointRegistry
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


class Source1:
    pass


class To1:
    pass


class To2:
    pass

if __name__ == '__main__':
    unittest.main()