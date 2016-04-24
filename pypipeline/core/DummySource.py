from .Source import Source


class DummySource(Source):
    def stop(self):
        pass

    def start(self):
        pass
