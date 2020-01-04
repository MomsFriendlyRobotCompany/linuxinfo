#!/usr/bin/env python

from linuxinfo import pi_info

r = pi_info()
if r is None:
    print("** This must not be a Raspberry Pi ??? **")
    exit(1)

print(r)
