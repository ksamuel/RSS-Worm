#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4


"""
    Init code for setting up the data dir and the database.
"""

import os

import settings


class RssWormInitError(Exception):
    pass


def setup_data_dir(data_dir=settings.DATA_DIR):
    """
        Create the data dir if no data dir exists
    """
    if not os.path.isdir(data_dir):
        try:
            os.makedirs(data_dir)
        except Exception as e:
            msg = (u"Unable to create directory %s: %s. "
                   u"Rss Worm cannot start." % (data_dir, str(e)))
            raise RssWormInitError(msg)


def setup_database(db_file_path=settings.DB_FILE_PATH):
    """
        Connect the database.

        Create the database tables if they don't exists already.
    """
    # import models here to avoid circular references
    from models import BaseModel, Feed, FeedItem

    BaseModel.db.connect()

    Feed.create_table()
    FeedItem.create_table()


def setup():
    setup_data_dir()
    setup_database()

