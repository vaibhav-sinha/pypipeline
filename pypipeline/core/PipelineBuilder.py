class PipelineBuilder:
    def __init__(self):
        self.source_class = None
        self.source_params = None
        self.to_list = []
        self.id = None
        self.auto_start = True

    def build(self):
        raise NotImplementedError

    def build_with_plumber(self, plumber):
        raise NotImplementedError