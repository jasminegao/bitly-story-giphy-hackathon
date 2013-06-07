"""
A simple request handler that will be access from javascript.
"""

import ujson as json
from flask import Flask
import bursting_phrase_fetcher

app = Flask(__name__)

api_key = open("api_key.txt").read()
phrase_fetcher = bursting_phrase_fetcher.BurstingPhraseFetcher(api_key=api_key)


@app.route('/bursting_phrases')
def bursting_phrases():
  phrases = phrase_fetcher.get_bursting_phrases()
  return 'Hello, world!' + " ".join(phrases)

if __name__ == "__main__":
  app.run()


