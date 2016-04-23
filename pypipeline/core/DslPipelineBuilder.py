from urllib.parse import urlparse
from . import EndpointRegistry
from .Pipeline import Pipeline
from .Source import Source
from .Destination import Destination
from.PipelineBuilder import PipelineBuilder


class DslPipelineBuilder(PipelineBuilder):

    def source(self, endpoint):
        assert isinstance(endpoint, str), "You need to provide an endpoint uri"
        assert self.source_class is None, "There can only be one source in a pipeline"
        uri = urlparse(endpoint)
        self.source_class = EndpointRegistry.get_endpoint(uri.scheme)
        self.source_uri = uri
        assert issubclass(self.source_class, Source), "The source class should be a subclass of Source"
        return self

    def to(self, endpoint):
        assert isinstance(endpoint, str), "You need to provide an endpoint uri"
        assert self.source_class is not None, "Pipeline definition must start with a source"
        uri = urlparse(endpoint)
        to_class = EndpointRegistry.get_endpoint(uri.scheme)
        self.to_list.append((to_class, uri))
        return self

    def process(self, method):
        assert callable(method), "You need to provide a callable function"
        assert self.source_class is not None, "Pipeline definition must start with a source"
        to_class = type("", (Destination,), {"process": lambda self, exchange: method(exchange)})
        uri = None
        self.to_list.append((to_class, uri))
        return self

    def id(self, name):
        self.id = name

    def auto_start(self, value):
        assert isinstance(value, bool), "auto_start parameter accepts only boolean values"
        self.auto_start = value

    def build(self):
        return self.buildWithPlumber(None)

    def buildWithPlumber(self, plumber):
        assert len(self.to_list) > 0, "Pipeline needs to have atleast one destination"
        return Pipeline(self, plumber)