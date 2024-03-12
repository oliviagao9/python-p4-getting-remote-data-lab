import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url 
    #sends a GET request to the URL passed in, return body of the response
    def get_response_body(self):
        URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(URL)
        return response.content

    #should use get_response_body to send a reqeust, return a Python list or dict
    def load_json(self):
        response_data = json.loads(self.get_response_body())
        return response_data