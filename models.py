#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

"""
    ORM layer to manipulate feeds and changes stored in the Sqlite database.
"""

import peewee

import settings


class BaseModel(peewee.Model):

    db = peewee.SqliteDatabase(settings.DB_FILE_PATH)

    class Meta:
        database = db


class Feed(BaseModel):
    url = peewee.CharField(max_length=256)
    title = peewee.CharField(max_length=64)
    version = peewee.CharField(max_length=8, null=True)
    description = peewee.TextField(null=True)
    recent_changes_link = peewee.CharField(max_length=256, null=True, 
                          help_text=(u"Url to a page associated witht the feed "
                                     u"that would list recents changes"))
    interwiki = peewee.CharField(max_length=128, null=True, 
                help_text=(u"For wiki, the wiki's preferred InterWiki moniker"))


    @classmethod
    def create_from_web_page(url):
        """
            Create a feed object, saves it and returns it.

            It use the url parameter to fetch the page from the web,
            extract the feed url from it and pass it to feedparser.

            From then it saves all the meta data on the DB.
        """
        
        

    def __unicode__(self):
        return self.title


class FeedItem(BaseModel):
    title = peewee.CharField(max_length=64)
    summary = peewee.TextField(null=True)
    content = peewee.TextField()
    publication_date = peewee.DateTimeField(help_text=(u"The date at which the "
                                     u"modification have been published"))
    fetching_date = peewee.DateTimeField(help_text=(u"The date at which the "
                                     u"rssworm fetch this item."))

    feed = peewee.ForeignKeyField(Feed, related_name='items')

    read = peewee.BooleanField(default=False)

    def __unicode__(self):
        return '%s: %s' % (self.feed.title, self.title)