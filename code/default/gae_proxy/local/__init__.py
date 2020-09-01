
from . import apis
from . import proxy


def is_ready():
    return proxy.ready


def start(args):
    proxy.main(args)


def stop():
    proxy.terminate()
