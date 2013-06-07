import requests
import json

api_key = "dc6zaTOxFJmzC"
endpoint = "http://api.giphy.com/v1/gifs/search"

class Giphy:
    
    def __init__(self, phrases, api_key):
    """
    phrases: A list of phrases for a story.
    """
        self._api_key = api_key
        self._phrases = []
        params = {"api_key": api_key}    
        response = requests.get(endpoint, params=params)    
        data = json.loads(response.content)

    def giphy_search():
        for item in phrases:
            item = phrase
            params = {
                'api_key': api_key,
                'q': phrase,
                'limit': 5
            }
        
            response = requests.get(endpoint, params=query_params)

            data = json.loads(response.content)

            gif_urls = []

            for item in data["data"][0:]:
                original_url = item["images"]["original"]["url"]
                gif_urls.append(original_url)
            
            return gif_urls


