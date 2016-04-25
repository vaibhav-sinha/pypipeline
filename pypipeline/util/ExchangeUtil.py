import copy
import uuid


def copy_exchange(ex):
    exchange = copy.copy(ex)
    exchange.id = uuid.uuid4()
    exchange.in_msg = copy.deepcopy(ex.in_msg)
    exchange.out_msg = copy.deepcopy(ex.out_msg)
    exchange.properties = copy.deepcopy(ex.properties)
    return exchange
