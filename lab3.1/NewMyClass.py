from BaseClient import BaseClient
import requests


class GetId(BaseClient):
    BASE_URL = "https://api.vk.com/method/"
    method = 'users.get'
    http_method = '?user_ids='
    username = None
    """vk_id = None"""

    def __init__(self):
        self.username = raw_input("Input user's name ")

    def generate_url(self):
        return '{0}{1}{2}{3}'.format(self.BASE_URL, self.method, self.http_method, self.username)

    def get_data(self):

        r = requests.get(self.generate_url()).json()
        try:
            if r["response"][0]["deactivated"]:
                print("this page was banned or not exist")
                exit()
        except Exception:
            return r["response"][0]["uid"]


class GetFriend(BaseClient):
    def __init__(self, vk_id):
        self.vk_id = vk_id
        self.get_data()

    BASE_URL = "https://api.vk.com/method/"
    method = 'friends.get'
    http_method = '?uid='
    fields = "&fields=bdate"

    def generate_url(self):
        return '{0}{1}{2}{3}{4}'.format(self.BASE_URL, self.method, self.http_method, self.vk_id, self.fields)

    def get_data(self):

        r = requests.get(self.generate_url()).json()
        return r["response"]

    def bdayArr(self):
        new_arr = []
        for friend in self.get_data():
            try:
                if len(friend["bdate"]) >= 8:
                    new_arr.append(friend["bdate"])

            except Exception:
                continue
        return new_arr
