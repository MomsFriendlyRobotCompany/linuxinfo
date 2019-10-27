from collections import namedtuple
from .helpers import un
import re
from .helpers import read


rpi_ids = {
    "900061": ("CM3", "512MB"),
    "a020a0": ("CM3", "1GB"),
    "a02100": ("CM3+", "1GB"),
    "900092": ("Zero", "512MB"),
    "900093": ("Zero", "512MB"),
    "9000c1": ("Zero W", "512MB"),
    "a02082": ("Pi3B", "1GB"),
    "a22082": ("Pi3B", "1GB"),
    "a32082": ("Pi3B", "1GB"),
    "a52082": ("Pi3B", "1GB"),
    "a22083": ("Pi3B", "1GB"),
    "a020d3": ("Pi3B+", "1GB"),
    "a03111": ("Pi4B", "1GB"),
    "b03111": ("Pi4B", "2GB"),
    "c03111": ("Pi4B", "4GB")
}


def is_pi():
    if un.sysname != 'Linux' or un.machine not in ["armv7l", "aarch64"]:
        return False
    return True


PiInfo = namedtuple("PiInfo", "name name_pretty hardware revision memory serial hostname arch")


def find(key, info):
    match = re.search('^{}\s+:\s+(\w+)$'.format(key), info, flags=(re.MULTILINE | re.IGNORECASE))
    return match.group(1)


def pi_info():
    if not is_pi():
        return None

    cpuinfo = read('/proc/cpuinfo')
    if cpuinfo is None:
        return None

    rev = find("Revision", cpuinfo)
    rpi = rpi_ids[rev]
    hw = find("Hardware", cpuinfo)
    ser = find("Serial", cpuinfo)
    mod = find("Model", cpuinfo)

    return PiInfo(rpi[0], mod, hw, rev, rpi[1], ser, un.nodename, un.machine)
