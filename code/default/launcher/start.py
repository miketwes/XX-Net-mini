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
sys.path.append(current_path)
sys.path.append(os.path.abspath(os.path.join(default_path, 'lib')))
ca_path = os.path.join(data_path, "gae_proxy")
ca_cert = os.path.join(ca_path, 'CA.crt')
ca_key = os.path.join(ca_path, 'CAkey.pem')
cert_keyfile = os.path.join(ca_path, 'Certkey.pem')
ca_openssl_cfg = os.path.join(ca_path, 'ca_openssl.config')


from xlog import getLogger
xlog = getLogger("launcher")


def uncaughtExceptionHandler(etype, value, tb):
    if etype == KeyboardInterrupt:  # Ctrl + C on console
        xlog.warn("KeyboardInterrupt, exiting...")
        module_init.stop_all()
        os._exit(0)

    exc_info = ''.join(traceback.format_exception(etype, value, tb))
    print(("uncaught Exception:\n" + exc_info))
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

    if not os.path.exists(ca_cert):

        import platform
        import subprocess
        import hashlib

        
        def runcmd(cmd):
        	p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE , stderr=subprocess.PIPE)
        	stdout, stderr = p.communicate()
        	return (stdout, stderr,p.returncode)
        
        commonname = 'GoAgent-XX-Net-mini-4.5.2'
        
        sn = '0x%s' % hashlib.md5((commonname + str(datetime.now())).encode("utf-8")).hexdigest()
        
        cmd = "openssl req -x509 -newkey rsa:2048 -sha256 -days 3650 -set_serial " + sn + " -nodes -keyout CA.key  -out " + ca_cert + " -extensions v3_req -config " + ca_openssl_cfg
        runcmd(cmd)
        cmd = "openssl genrsa  -out p.key 2048"
        runcmd(cmd)
        cmd = "openssl rsa -in p.key -pubout -out pub.key"
        runcmd(cmd)
        
        
        filenames = [ca_cert, 'CA.key']
        with open(ca_key, 'wb') as outfile:
            for fname in filenames:
                with open(fname, 'rb') as infile:
                    outfile.write(infile.read())
        
        filenames = ['p.key', 'pub.key']
        with open(cert_keyfile, 'wb') as outfile:
            for fname in filenames:
                with open(fname, 'rb') as infile:
                    outfile.write(infile.read())
        
        os.remove('CA.key')
        os.remove('p.key')
        os.remove('pub.key')
        
        if(platform.system()=='Windows'):
            cmd = "certmgr /c /add " + ca_cert + " /s root"
            runcmd(cmd)
        elif(platform.system()=='Linux'):
            cmd = 'certutil -d sql:$HOME/.pki/nssdb -A -t "CT,C,c" -n ' + commonname + ' -i '  + ca_cert
            runcmd(cmd)
        else:
            pass

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
