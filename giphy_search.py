import requests
import json

api_key = "dc6zaTOxFJmzC"
giphy_search_url = "http://api.giphy.com/v1/gifs/search"

class Giphy:
    def __init__(self, api_key=api_key):
        """
        phrases: A list of phrases for a story.
        """
        self._api_key = api_key

    def giphy_search(self, phrases):
        for phrase in phrases:
            query_params = {
                'api_key': api_key,
                'q': phrase,
                'limit': 5
            }
            response = requests.get(giphy_search_url, params=query_params)

            data = json.loads(response.content)

            gif_urls = []

            for item in data["data"][0:]:
                original_url = item["images"]["original"]["url"]
                gif_urls.append(original_url)

            return gif_urls


