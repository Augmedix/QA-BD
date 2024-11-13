
# Google Search API endpoint for testing purposes
import requests

class GoogleSearchEndpoint:
    """
    Class to represent the Google Search API endpoint.
    Provides methods to perform search operations via API calls.
    """
    def __init__(self, base_url, api_key):
        """Initialize with the base URL and API key."""
        self.base_url = base_url
        self.api_key = api_key

    def search(self, query):
        """Perform a search query on the API."""
        params = {"key": self.api_key, "q": query}
        return requests.get(f"{self.base_url}", params=params)

# FAQ:
# Q: Why use a class to represent the API endpoint?
# A: It makes the endpoint modular and reusable in multiple tests.
# Q: Where should the API key be stored?
# A: In environment variables.
