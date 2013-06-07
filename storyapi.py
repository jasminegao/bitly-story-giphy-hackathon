"""
  Access the bitly story API.

"""

import requests
from collections import defaultdict

STORY_FROM_PHRASES_URL = "https://api-ssl.bitly.com/v3/story_api/story_from_phrases"
STORY_PHRASES_URL = "https://api-ssl.bitly.com/v3/story_api/distribution"
STORY_METADATA_URL = "https://api-ssl.bitly.com/v3/story_api/metadata"

class Story:

  def __init__(self, phrases, access_token):
    """
     phrases: A list of phrases this story will be created from.
    """
    self._access_token = access_token
    self._story_id = None
    self._story_phrases = []
    params = {"access_token": access_token, "phrases": phrases[0]}
    response = requests.get(STORY_FROM_PHRASES_URL, params=params)
    data = response.json()
    if not self.check_status(data):
      return
    self._story_id = data['data']['story_id']

  def get_story_phrases(self,limit=10):
    if not self._story_id:
      return
    params = {"access_token": self._access_token,
              "field": "phrases",
              "story_id":self._story_id,
              "limit":limit,
              }
    response = requests.get(STORY_PHRASES_URL, params=params)
    data = response.json()
    if not self.check_status(data):
      return
    phrases = []
    for phrase, rate in data['data']['phrases']:
      if not phrase == "_COUNT_":
        phrases.append(phrase)
    self._phrases = phrases
    return phrases

  def get_story_rates(self):
        params = {"access_token": self._access_token,
                  "story_id": self._story_id,
                  "field": "rates"
                  }
        response = requests.get(STORY_METADATA_URL, params=params)
        data = response.json()
        if not self.check_status(data):
            return
        rates = data['data']['rates']
        self._rates = rates
        return rates

  def check_status(self, response):
    if response["status_txt"] != "OK":
      print "WARNING: request failed: %s" % response["status_txt"]
      return False
    return True


