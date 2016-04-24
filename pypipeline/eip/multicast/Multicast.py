class Multicast:
    def __init__(self, plumber, params):
        self.plumber = plumber
        self.params = params
        self.aggregator = params["aggregator"](plumber, {})
        self.pipelines = []
        for builder in params["pipelines"]:
            self.pipelines.append(builder.build_with_plumber(plumber))