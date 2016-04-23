import uuid


class Exchange:
    def __init__(self):
        self.id = uuid.uuid4()
        self.in_msg = None
        self.out_msg = None
        self.properties = {}