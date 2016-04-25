import uuid


class Exchange:
    def __init__(self):
        self.id = uuid.uuid4()
        self.in_msg = None
        self.out_msg = None
        self.properties = {}

    def __str__(self):
        return "Id: " + str(self.id) + "\nProperties: " + str(self.properties) + "\nIn Msg:\n" + str(self.in_msg) + "\nOut Msg:\n" + str(self.out_msg)