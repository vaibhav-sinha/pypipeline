class PipelineBuilder:
    def __init__(self):
        self.source_class = None
        self.source_uri = None
        self.to_list = []
        self.id = None
        self.auto_start = True

    def build(self):
        raise NotImplementedError

    def buildWithPlumber(self, plumber):
        raise NotImplementedError