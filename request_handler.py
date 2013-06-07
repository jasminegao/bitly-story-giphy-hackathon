"""
A simple request handler that will be access from javascript.
"""

from flask import Flask
from flask import render_template
import bursting_phrase_fetcher
import storyapi
import giphy_search

app = Flask(__name__)

api_key = open("api_key.txt").read()
access_token = open("access_token.txt").read()

phrase_fetcher = bursting_phrase_fetcher.BurstingPhraseFetcher(api_key=api_key)
giphy = giphy_search.Giphy()


@app.route('/bursting_phrases')
def bursting_phrases():
  phrases = phrase_fetcher.get_bursting_phrases()
  return 'Hello, world!' + " ".join(phrases)


@app.route('/get_story_gifs')
def bursting_phrases():
  phrases = phrase_fetcher.get_bursting_phrases()
  stories = [storyapi.Story([phrase],access_token=access_token) for phrase in phrases]

  #TODO: sort the stories by click rate
  for story in stories:
    story.rt_url = "http://rt.ly/story?story_id=" + story._story_id
    story.phrases = story.get_story_phrases()
    #story.rates = story.get_story_rates()
    story_gifs = giphy.giphy_search(story.phrases)
    story.gif_urls = story_gifs

  return render_template("stories.html",stories=stories)


if __name__ == "__main__":
  app.run()


