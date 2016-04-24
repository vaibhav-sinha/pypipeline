class ContentBasedRouter:
    def __init__(self, plumber, params):
        self.branches = []
        self.plumber = plumber
        for condition, builder in params["branches"]:
            self.branches.append((condition, builder.build_with_plumber(plumber)))

    def get_valid_pipeline(self, exchange):
        for condition, pipeline in self.branches:
            valid = condition(exchange)
            if valid:
                return pipeline
        return None
