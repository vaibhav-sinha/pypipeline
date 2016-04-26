PyPipeline's - ESB for Python
=============================

PyPipeline is an Enterprise Service Bus for Python. It is inspired from the Apache Camel project for Java. Like Camel,
PyPipeline provides an intuitive Domain Specific Language to build a pipeline.

Here is an example which creates and runs a pipeline::

   builder = DslPipelineBuilder()
   pipeline = builder.source(Timer, {"period": 1.0}).to(Log, {"name": "test"}).build()
   pipeline.start()
   time.sleep(10)
   pipeline.stop()

In the example, an instance of DslPipelineBuilder is created (This is the only PipelineBuilder implementation
available right now. Later a YAML based PipelineBuilder might be added), which is used to specify the pipeline structure.

For any pipeline, a source is needed, which produces data that is to be sent down the pipe. In the example, the source is
a Timer which is configured to produce data every 1 second. The data is then sent to a Log Destination, which prints the
data to standard out.

The pipeline is then started, which triggers the Timer to start sending data. After 10 seconds, the pipeline is stopped.

Enterprise Integration Patterns
===============================

PyPipeline intends to support all of patterns from the Enterprise Integration Patterns book by Gregor Hohpe and Booby Woolf.

Currently the following patterns are supported

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

Concepts:
=========

.. toctree::
   :maxdepth: 4
   core
   eip
   component


