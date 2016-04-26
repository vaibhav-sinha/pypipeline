# PyPipeline - ESB for Python

### PyPipeline is for Python, what Apache Camel is for Java.

[![Build Status](https://travis-ci.org/vaibhav-sinha/pypipeline.svg?branch=master)](https://travis-ci.org/vaibhav-sinha/pypipeline)

PyPipeline is meant to be a lightweight ESB, configurable via an intutive DSL. PyPipeline implements many of the [Enterprise Integration Patterns](http://www.eaipatterns.com/toc.html).

Currently supported EIPs are:

* Filter
* Aggregator
* Splitter
* Multicast
* Content Based Router
* Routing Slip
* Dynamic Router
* Resequencer
* Validator
* Wiretap

Following EIPs can be implemented using the patterns listed above:

* Recipient List
* Composed Message Processor
* Scatter Gather
* Content Enricher
* Content Filter
* Claim Check
* Normalizer
* Detour
* Log


## Getting Started

Creating pipelines with PyPipeline is very simple. Here is an example to a pipeline in which a timer generates a data packet every one second which is then sent to a filter, and finally the packets which are not filtered out go to a log component which prints them on the console

    class FilterTest(unittest.TestCase):

        def test_simple_pipeline(self):
            builder = DslPipelineBuilder()
            pipeline = builder.source(Timer, {"period": 1.0}).filter(filter_method).process(Log, {"name": "test"}).build()
            pipeline.start()
            time.sleep(10)
            pipeline.stop()


    def filter_method(exchange):
        parts = exchange.in_msg.body.split()
        return int(parts[-1]) % 2 == 0


## Documentation

The documentation can be found at [PyPipeline Documentation](http://pypipeline-esb.readthedocs.org/en/latest/)
