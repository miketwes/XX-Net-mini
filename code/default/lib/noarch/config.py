import os
import sys
import json

current_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.abspath(os.path.join(current_path, os.pardir, os.pardir, os.pardir, os.pardir, 'data'))
jsonfile = os.path.join(data_path, 'config.json')


config = sys.modules[__name__]

with open(jsonfile, 'r') as f:
    t = json.load(f)
for n in t:
    setattr(config, n, t[n])

setattr(config, 'GAE_APPIDS', [i for i in config.gaeappids])
setattr(config, 'CHECK_PKP', set(str(i).encode() for i in config.check_pkp))
setattr(config, 'HOSTS_GAE', tuple(str(i).encode() for i in config.hosts_gae))
setattr(config, 'HOSTS_DIRECT', tuple(str(i).encode() for i in config.hosts_direct))
setattr(config, 'HOSTS_GAE_ENDSWITH', tuple(str(i).encode() for i in config.hosts_gae_endswith))
setattr(config, 'HOSTS_DIRECT_ENDSWITH', tuple(str(i).encode() for i in config.hosts_direct_endswith))
setattr(config, 'GOOGLE_ENDSWITH', tuple(str(i).encode() for i in config.google_endswith))
setattr(config, 'br_sites', tuple(str(i).encode() for i in config.BR_SITES))
setattr(config, 'br_endswith', tuple(str(i).encode() for i in config.BR_SITES_ENDSWITH))
