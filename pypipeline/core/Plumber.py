from .Status import Status
from .Exchange import Exchange
from .PipelineBuilder import PipelineBuilder


class Plumber:
    def __init__(self):
        self.pipelines = {}
        self.state = Status.stopped

    def create_exchange(self):
        exchange = Exchange()
        exchange.plumber = self
        return exchange

    def start(self):
        self.state = Status.starting
        for pipeline_id, pipeline in self.pipelines.items():
            self._start_pipeline(pipeline)
        self.state = Status.running

    def stop(self):
        self.state = Status.stopping
        for pipeline_id, pipeline in self.pipelines.items():
            self._stop_pipeline(pipeline)
        self.state = Status.stopped

    def add_pipeline(self, pipeline):
        if isinstance(pipeline, PipelineBuilder):
            pipeline = pipeline.buildWithPlumber(self)
        if pipeline.id is None:
            pipeline.id = "pipeline" + str(len(self.pipelines) - 1)
        self.pipelines[pipeline.id] = pipeline
        if pipeline.auto_start and self.state in (Status.running, Status.starting):
            self._start_pipeline(pipeline)

    def _start_pipeline(self, pipeline):
        assert pipeline is not None, "Pipeline is not found"
        if self.state not in (Status.running, Status.starting):
            raise ValueError("Plumber is not in running state")
        pipeline.start()

    def start_pipeline(self, id):
        self._start_pipeline(self.pipelines[id])

    def _stop_pipeline(self, pipeline):
        assert pipeline is not None, "Pipeline is not found"
        if self.state not in (Status.running, Status.stopping):
            raise ValueError("Plumber is not in running state")
        pipeline.stop()

    def stop_pipeline(self, id):
        self._stop_pipeline(self.pipelines[id])