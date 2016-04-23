registry = {

}


def add_endpoint(name, clazz):
    registry[name] = clazz


def get_endpoint(name):
    return registry[name]