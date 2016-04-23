from enum import Enum


class Status(Enum):
    starting = 1
    stopping = 2
    running = 3
    stopped = 4