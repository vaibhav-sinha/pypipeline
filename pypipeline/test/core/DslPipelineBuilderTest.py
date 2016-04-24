import unittest
from pypipeline.core.DslPipelineBuilder import DslPipelineBuilder
from pypipeline.core.Source import Source
from pypipeline.core.Destination import Destination
import inspect


class DslPipelineDefinitionBuilderTest(unittest.TestCase):

    def test_simple_pipeline(self):
        builder = DslPipelineBuilder()
        builder.source({"endpoint": Source1}).to({"endpoint": To1}).to({"endpoint": To2})
        self.assertEqual(builder.source_class, Source1)

    def test_process_block(self):
        builder = DslPipelineBuilder()
        builder.source({"endpoint": Source1}).to({"endpoint": To1}).to({"endpoint": To2}).process(lambda x: print(x))
        self.assertEqual(builder.source_class, Source1)
        self.assertTrue(inspect.isclass(builder.to_list[2][0]))

    def test_one_source(self):
        builder = DslPipelineBuilder()
        with self.assertRaises(AssertionError):
            builder.to({"endpoint": To1})

    def test_only_one_source(self):
        builder = DslPipelineBuilder()
        with self.assertRaises(AssertionError):
            builder.source({"endpoint": To1}).source({"endpoint": To1})

    def test_build_pipeline(self):
        builder = DslPipelineBuilder()
        pipeline = builder.source({"endpoint": Source1}).to({"endpoint": To1}).to({"endpoint": To2}).build()
        self.assertIsNotNone(pipeline.source.chain)

    def test_multicast_dsl(self):
        builder = DslPipelineBuilder()
        builder.source({"endpoint": Source1}).to({"endpoint": To1}).multicast({})\
            .pipeline().to({"endpoint": To1}).to({"endpoint": To1}).end_pipeline()\
            .pipeline().to({"endpoint": To1}).to({"endpoint": To1}).end_pipeline()\
            .end_multicast().to({"endpoint": To1})
        self.assertIsNotNone(builder.builder_stack[-1])


class Source1(Source):
    pass


class To1(Destination):
    pass


class To2(Destination):
    pass

if __name__ == '__main__':
    unittest.main()