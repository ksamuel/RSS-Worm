#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

"""
    Centralised module for all the static RSS WORM settings. Not meant
    to be edited by the user.
"""

import os

# todo: make it a hidden dir 
# (http://www.daniweb.com/software-development/python/threads/180031)
DATA_DIR = os.path.expanduser('~/.rssworm') 
DB_FILE_PATH = os.path.join(DATA_DIR, 'db.sqlite')