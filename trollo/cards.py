#!/usr/bin/env python
# Copyright (c) 2012, Fog Creek Software, Inc.
# Copyright (c) 2016-2018, Red Hat, Inc.
#   License: 2-clause BSD; see LICENSE.txt for details
import json
import requests


class Cards(object):
    __module__ = 'trollo'

    def __init__(self, apikey, token=None):
        self._apikey = apikey
        self._token = token

    def copy(self, card_id, list_id):
        resp = requests.post("https://trello.com/1/cards",
                             params=dict(key=self._apikey, token=self._token,
                                         idList=list_id, idCardSource=card_id))
        resp.raise_for_status()
        return json.loads(resp.content)

    def get(self, card_id, actions=None, action_fields=None, action_limit=None,
            attachments=None, attachment_fields=None, members=None,
            member_fields=None, checkItemStates=None,
            checkItemState_fields=None, checklists=None, checklist_fields=None,
            fields=None):
        resp = requests.get("https://trello.com/1/cards/%s" % (card_id),
                            params=dict(key=self._apikey, token=self._token,
                                        actions=actions,
                                        action_fields=action_fields,
                                        action_limit=action_limit,
                                        attachments=attachments,
                                        attachment_fields=attachment_fields,
                                        members=members,
                                        member_fields=member_fields,
                                        checkItemStates=checkItemStates,
                                        checkItemState_fields=checkItemState_fields,
                                        checklists=checklists,
                                        checklist_fields=checklist_fields,
                                        fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_field(self, field, card_id):
        resp = requests.get("https://trello.com/1/cards/%s/%s" % (card_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_action(self, card_id, filter=None, fields=None, limit=None, page=None, idModels=None):
        resp = requests.get("https://trello.com/1/cards/%s/actions" % (card_id), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, limit=limit, page=page, idModels=idModels), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_attachment(self, card_id, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/attachments" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board(self, card_id, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/board" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_board_field(self, field, card_id):
        resp = requests.get("https://trello.com/1/cards/%s/board/%s" % (card_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_checkItemState(self, card_id, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/checkItemStates" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_checklist(self, card_id, cards=None, card_fields=None, checkItems=None, checkItem_fields=None, filter=None, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/checklists" % (card_id), params=dict(key=self._apikey, token=self._token, cards=cards, card_fields=card_fields, checkItems=checkItems, checkItem_fields=checkItem_fields, filter=filter, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list(self, card_id, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/list" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_list_field(self, field, card_id):
        resp = requests.get("https://trello.com/1/cards/%s/list/%s" % (card_id, field), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def get_member(self, card_id, fields=None):
        resp = requests.get("https://trello.com/1/cards/%s/members" % (card_id), params=dict(key=self._apikey, token=self._token, fields=fields), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update(self, card_id, name=None, desc=None, closed=None, idList=None, due=None, pos=None):
        req_data = dict(name=name, desc=desc, closed=closed, idList=idList, due=due)

        if pos:
            req_data['pos'] = pos

        resp = requests.put("https://trello.com/1/cards/%s" % (card_id), params=dict(key=self._apikey, token=self._token), data=req_data)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_closed(self, card_id, value):
        resp = requests.put("https://trello.com/1/cards/%s/closed" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_desc(self, card_id, value):
        resp = requests.put("https://trello.com/1/cards/%s/desc" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_due(self, card_id, value):
        resp = requests.put("https://trello.com/1/cards/%s/due" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_idList(self, card_id, value):
        resp = requests.put("https://trello.com/1/cards/%s/idList" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_pos(self, card_id, pos):
        resp = requests.put("https://trello.com/1/cards/%s/pos" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=pos))
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_customField(self, card_id, custom_field_id, value):
        data = None
        if isinstance(value, dict):
            data = dict(value=value)
        else:
            data = dict(idValue=value)

        resp = requests.put("https://trello.com/1/cards/%s/customField/%s/item" % (card_id, custom_field_id), params=dict(key=self._apikey, token=self._token), data=data)
        resp.raise_for_status()
        return json.loads(resp.content)

    def update_name(self, card_id, value):
        resp = requests.put("https://trello.com/1/cards/%s/name" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def check_checkItem(self, card_id, idCheckItem):
        resp = requests.put("https://trello.com/1/cards/%s/checkItem/%s" % (card_id, idCheckItem), params=dict(key=self._apikey, token=self._token), data=dict(state="complete"))
        resp.raise_for_status()
        return json.loads(resp.content)

    def uncheck_checkItem(self, card_id, idCheckItem):
        resp = requests.put("https://trello.com/1/cards/%s/checkItem/%s" % (card_id, idCheckItem), params=dict(key=self._apikey, token=self._token), data=dict(state="incomplete"))
        resp.raise_for_status()
        return json.loads(resp.content)

    def rename_checkItem(self, card_id, idCheckItem, new_name):
        resp = requests.put("https://trello.com/1/cards/%s/checkItem/%s" % (card_id, idCheckItem), params=dict(key=self._apikey, token=self._token), data=dict(name=new_name))
        resp.raise_for_status()
        return json.loads(resp.content)

    def move_checkItem(self, card_id, idCheckItem, position):
        """
        Valid postions: 'top', 'bottom' or a positive number
        """
        resp = requests.put("https://trello.com/1/cards/%s/checkItem/%s" % (card_id, idCheckItem), params=dict(key=self._apikey, token=self._token), data=dict(pos=str(position)))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new(self, name, idList, desc=None):
        resp = requests.post("https://trello.com/1/cards" % (), params=dict(key=self._apikey, token=self._token), data=dict(name=name, idList=idList, desc=desc))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_action_comment(self, card_id, text):
        resp = requests.post("https://trello.com/1/cards/%s/actions/comments" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(text=text))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_attachment(self, card_id, url, name):
        resp = requests.post("https://trello.com/1/cards/%s/attachments" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(url=url, name=name))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_checklist(self, card_id, name):
        resp = requests.post("https://trello.com/1/cards/%s/checklists" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(name=name))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_label(self, card_id, value):
        resp = requests.post("https://trello.com/1/cards/%s/labels" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_label_idLabel(self, card_id_or_shortlink, value):
        resp = requests.post("https://trello.com/1/cards/%s/idLabels" % (card_id_or_shortlink), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_member(self, card_id, value):
        resp = requests.post("https://trello.com/1/cards/%s/idMembers" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def new_membersVoted(self, card_id, value):
        resp = requests.post("https://trello.com/1/cards/%s/membersVoted" % (card_id), params=dict(key=self._apikey, token=self._token), data=dict(value=value))
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete(self, card_id):
        resp = requests.delete("https://trello.com/1/cards/%s" % (card_id), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_checklist_idChecklist(self, idChecklist, card_id):
        resp = requests.delete("https://trello.com/1/cards/%s/checklists/%s" % (card_id, idChecklist), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_label_color(self, color, card_id):
        resp = requests.delete("https://trello.com/1/cards/%s/labels/%s" % (card_id, color), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_label_idLabel(self, idLabel, card_id_or_shortlink):
        resp = requests.delete("https://trello.com/1/cards/%s/idLabels/%s" % (card_id_or_shortlink, idLabel), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_member_idMember(self, idMember, card_id):
        resp = requests.delete("https://trello.com/1/cards/%s/members/%s" % (card_id, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)

    def delete_membersVoted_idMember(self, idMember, card_id):
        resp = requests.delete("https://trello.com/1/cards/%s/membersVoted/%s" % (card_id, idMember), params=dict(key=self._apikey, token=self._token), data=None)
        resp.raise_for_status()
        return json.loads(resp.content)
