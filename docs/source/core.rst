PyPipeline Core
===============

PyPipeline has five major concepts

1. Components/Endpoints
2. Exchange
3. Pipeline
4. EIP
5. Plumber

Components/Endpoints
--------------------

Components are the blocks which either produce, process or consume data that flows on the bus. In PyPipeline, the components
can be of two types:

Source
^^^^^^

A source is a component which produces data that will flow on the bus. How the data is generated is completely up to the
source. Few examples of how sources may generate data are as follows

* A MySQL source component may read a table from a database and send each row as one data packet.
* A RabbitMQ source may listen to a queue and produce a data packet for every message received from the queue.
* A REST source may access an API and send the response as a data packet

The sources continuously run, until explicitly stopped, and are event based. They run their own thread, which responds
to some event (a message on the queue, in case of RabbitMQ source) and produce data packets.

A source might take some parameters for configuration, such as database name, host and port in case of MySQL source.

When implementing any source, the class must extend the Source class from *core* package.::

    class Source:
        def __init__(self, plumber, params):
            self.plumber = plumber
            self.chain = None
            self.params = params

        def start(self):
            raise NotImplementedError("Sources should implement their start method")

        def stop(self):
            raise NotImplementedError("Sources should implement their stop method")


When start is called, the source must start it's own thread which listens to the events and produces data packets. To send
the data of the bus, it must call the *process* method of *self.chain*.

When stop is called, the source must stop the thread and not send any more data packets on the bug.

Destination
^^^^^^^^^^^

A destination is a component which receives a data packet as input and processes it to either modify the data, or send it
an external service, or both. Few examples of destination are as follows

* A MongoDB destination component which receives json data and persists it in a collection
* A reverse geocoder destination which modifies the data to convert it location field from lat/long to address
* A log destination component which prints the content of the data on console

A destination may take some parameters for configuration, such as collection name, host and port in case of MongoDB destination.

When implementing any destination, the class must extend the Destination class from *core* package.::

    class Destination:
        def __init__(self, plumber, params):
            self.plumber = plumber
            self.params = params

        def process(self, exchange):
            raise NotImplementedError("Subclass of destination needs to implement process method")

The destination class should implement it's logic in the *process* method.