#!/usr/bin/env python
# Copyright (c) 2012, Fog Creek Software, Inc.
# Copyright (c) 2016-2018, Red Hat, Inc.
#   License: 2-clause BSD; see LICENSE.txt for details
from .actions import Actions
from .boards import Boards
from .cards import Cards
from .checklists import Checklists
from .lists import Lists
from .members import Members
from .labels import Labels
from .notifications import Notifications
from .organizations import Organizations
from .search import Search
from .tokens import Tokens
from .types import Types

import sys
if sys.version_info < (3, 0):
    from urllib import quote_plus
else:
    from urllib.parse import quote_plus

__version__ = '0.2.5'


class TrelloApi(object):
    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token
        self.actions = Actions(apikey, token)
        self.boards = Boards(apikey, token)
        self.cards = Cards(apikey, token)
        self.checklists = Checklists(apikey, token)
        self.lists = Lists(apikey, token)
        self.members = Members(apikey, token)
        self.labels = Labels(apikey, token)
        self.notifications = Notifications(apikey, token)
        self.organizations = Organizations(apikey, token)
        self.search = Search(apikey, token)
        self.tokens = Tokens(apikey, token)
        self.types = Types(apikey, token)

    def set_token(self, token):
        self._token = token
        self.actions._token = token
        self.boards._token = token
        self.cards._token = token
        self.checklists._token = token
        self.lists._token = token
        self.members._token = token
        self.labels._token = token
        self.notifications._token = token
        self.organizations._token = token
        self.search._token = token
        self.tokens._token = token
        self.types._token = token

    def get_token_url(self, app_name, expires='30days', write_access=True):
        return 'https://trello.com/1/authorize?key=%s&name=%s&expiration=%s&response_type=token&scope=%s' % (self._apikey, quote_plus(app_name), expires, 'read,write' if write_access else 'read')
