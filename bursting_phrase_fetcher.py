#!/bin/env python
"""
  Interface for all http calls to the relevant bitly APIs,
  e.g. the storyapi and the burstingapi.
"""

import ujson as json
from tornado.httpclient import HTTPClient
import urllib
from collections import defaultdict


STORY_SERVER = "api-ssl.bitly.com"
BURSTING_SERVER = "rt.ly"

class BurstingPhraseFetcher:
  def __init__(self, access_token=None, api_key=None):
    self._hc = HTTPClient()
    self._access_token = access_token
    self._api_key = api_key

  def check_status(self, response):
    if response["status_txt"] != "OK":
      print "WARNING: request failed: %s" % response["status_txt"]
      return False
    return True


  def get_hot_phrases(self):
    url = "http://" + BURSTING_SERVER  + "/data/recentphrases" + "?"

    if self._api_key:
      params["api_key"] = self._api_key
    if self._access_token:
      params["access_token"] = self._access_token

    request_url = url + urllib.urlencode(params)
    data_raw = self._hc.fetch(request_url)
    data = json.loads(data_raw.body)
    check_status(data)
    if 'data' in data and 'phrases' in data['data']:
      phrases = data['data']['phrases']
      return phrases
    return []


  def get_bursting_phrases_data(self):
    url = "http://" + BURSTING_SERVER  + "/data/bursts" + "?"
    params = {}
    if self._api_key:
      params["api_key"] = self._api_key
    if self._access_token:
      params["access_token"] = self._access_token

    request_url = url + urllib.urlencode(params)
    data_raw = self._hc.fetch(request_url)
    data = json.loads(data_raw.body)
    if not self.check_status(data):
      return []
    if 'data' in data and 'phrases' in data['data']:
      phrases = data['data']['phrases']
      return phrases
      print request_url
    return []

  def get_bursting_phrases(self):
    phrase_data = self.get_bursting_phrases_data()
    phrases = []
    for d in phrase_data:
      phrases.append(d['phrase'])
    return phrases






