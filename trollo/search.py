#!/usr/bin/env python
# Copyright (c) 2021, Red Hat, Inc.
#   License: 2-clause BSD; see LICENSE.txt for details
import json
import requests


class Search(object):
    __module__ = 'trollo'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def run(self, query, **kwargs):
        resp = requests.get("https://trello.com/1/search", params=dict(key=self._apikey, token=self._token, query=query, **kwargs), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    # TODO - members
