import requests
import json

class ChronicleEntry(object):
    def __init__(self, data_dict, headers, cookies, api_url):
        self.headers = headers
        self.cookies = cookies
        self.API_URL = api_url
        self.episode = data_dict.get('episode', None)
        self.anime_id = data_dict.get('id', None)
        self.anime_title = data_dict.get('anime_title', None)
        self.ep_title = data_dict.get('ep_title', None)
        self.chronicle_id = data_dict.get('chronicle_id', None)
        try: 
            self.date = datetime.utcfromtimestamp(data_dict['date'])
        except:
            self.date = None

    def __post(self, data):
        with requests.post(self.API_URL, headers=self.headers, json=data, cookies=self.cookies) as url:
            return json.loads(url.text)

    def __repr__(self):
        return f'<ChronicleEntry: {self.chronicle_id}>'

    def remove_chronicle_entry(self):
        data = {
            "controller": "Profile",
            "action": "removeChronicleEntry",
            "chronicle_id": self.chronicle_id,
        }
        return self.__post(data)
