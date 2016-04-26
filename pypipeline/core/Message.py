class Message:
    def __init__(self):
        self.headers = {}
        self.body = None

    def __str__(self):
        return "\tHeaders: " + str(self.headers) + "\n\tBody: " + str(self.body)