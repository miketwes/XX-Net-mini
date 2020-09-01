import os
import sys
import time
import traceback
from datetime import datetime
import atexit

# reduce resource request for threading
# for OpenWrt
import threading
try:
    threading.stack_size(128 * 1024)
except:
    pass

try:
    import tracemalloc
    tracemalloc.start(10)
except:
    pass

current_path = os.path.dirname(os.path.abspath(__file__))
default_path = os.path.abspath(os.path.join(current_path, os.pardir))
data_path = os.path.abspath(os.path.join(default_path, os.pardir, os.pardir, 'data'))
data_launcher_path = os.path.join(data_path, 'launcher')
noarch_lib = os.path.abspath(os.path.join(default_path, 'lib', 'noarch'))
sys.path.append(noarch_lib)






from xlog import getLogger

xlog = getLogger("launcher")


def uncaughtExceptionHandler(etype, value, tb):
    if etype == KeyboardInterrupt:  # Ctrl + C on console
        xlog.warn("KeyboardInterrupt, exiting...")
        module_init.stop_all()
        os._exit(0)

    exc_info = ''.join(traceback.format_exception(etype, value, tb))
    print(("uncaught Exception:\n" + exc_info))
    with open(os.path.join(data_launcher_path, "error.log"), "a") as fd:
        now = datetime.now()
        time_str = now.strftime("%b %d %H:%M:%S.%f")[:19]
        fd.write("%s type:%s value=%s traceback:%s" % (time_str, etype, value, exc_info))
    xlog.error("uncaught Exception, type=%s value=%s traceback:%s", etype, value, exc_info)
    # sys.exit(1)


sys.excepthook = uncaughtExceptionHandler


has_desktop = False


def unload(module):
    for m in list(sys.modules.keys()):
        if m == module or m.startswith(module + "."):
            del sys.modules[m]

    for p in list(sys.path_importer_cache.keys()):
        if module in p:
            del sys.path_importer_cache[p]

    try:
        del module
    except:
        pass




from config import config

import module_init


def exit_handler():
    print('Stopping all modules before exit!')
    module_init.stop_all()


atexit.register(exit_handler)


def main():
    # change path to launcher
    global __file__
    __file__ = os.path.abspath(__file__)
    if os.path.islink(__file__):
        __file__ = getattr(os, 'readlink', lambda x: x)(__file__)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))


    allow_remote = 0
    no_mess_system = 0


    module_init.xargs["no_mess_system"] = 1

    restart_from_except = False

    module_init.start_all_auto()

    while True:
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:  # Ctrl + C on console
        module_init.stop_all()
        os._exit(0)
        sys.exit()
    except Exception as e:
        xlog.exception("launcher except:%r", e)
        input("Press Enter to continue...")
