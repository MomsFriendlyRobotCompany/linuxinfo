# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2019 Kevin Walchko
# see LICENSE for full details
##############################################

def read(filename):
    try:
        with open(filename, 'r') as fd:
            info = fd.read()
    except FileNotFoundError:
        info = None
    return info
