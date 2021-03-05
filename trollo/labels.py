#!/usr/bin/env python
# Copyright (c) 2021, Red Hat, Inc.
#   License: 2-clause BSD; see LICENSE.txt for details
import json

import requests


class Labels(object):
    __module__ = 'trollo'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def get(self, label_id):
        resp = requests.get("https://trello.com/1/labels/%s" % (label_id), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, label_id, name=None, color=None):
        if (name and color) or (not name and not color):
            resp = requests.put("https://trello.com/1/labels/%s" % (label_id), params=dict(key=self._apikey, token=self._token, name=name, color=color), data=None)
        elif name:
            resp = requests.put("https://trello.com/1/labels/%s/name" % (label_id), params=dict(key=self._apikey, token=self._token, value=name), data=None)
        elif color:
            resp = requests.put("https://trello.com/1/labels/%s/color" % (label_id), params=dict(key=self._apikey, token=self._token, value=color), data=None)

        resp.raise_for_status()
        return json.loads(resp.content)

    def delete(self, label_id):
        resp = requests.delete("https://trello.com/1/labels/%s" % (label_id), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)
