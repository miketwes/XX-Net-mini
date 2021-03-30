import time
import random

from front_base.connect_manager import NoRescourceException
from front_base.random_get_slice import RandomGetSlice


class HostManagerBase(object):

    def get_sni_host(self, ip):
        return None, ""


class SniManager(object):
    plus = ['-', '', "."]
    end = ["com", "net", "ml", "org", "us"]

    def __init__(self, logger):
        self.logger = logger
        self.slice = RandomGetSlice("sni_slice.txt", 20, '|')

    def get(self):
        return None

        n = random.randint(2, 3)
        ws = []
        for i in range(0, n):
            w = self.slice.get()
            ws.append(w)

        p = random.choice(self.plus)

        name = p.join(ws)
        name += "." + random.choice(self.end)

        return name


class HostManager(HostManagerBase):
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.appid_manager = None

        self.sni_manager = SniManager(logger)

    def get_host(self):
        if not self.appid_manager:
            return ""

        appid = self.appid_manager.get()
        if not appid:
            self.logger.warn("no appid")
            time.sleep(10)
            raise NoRescourceException("no appid")

        return appid + ".appspot.com"

    def get_sni_host(self, ip):
        sni = self.sni_manager.get()
        host = self.get_host()

        return sni, host

