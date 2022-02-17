import requests
from utils.configs_reader import DataReader


class GotoBin:

    def __init__(self):
        self.dread = DataReader()
        self.headers_bearer = {'Content-Type': 'application/json',
                               'Authorization': 'Bearer '+self.dread.bearer_token}
        self.headers_post = {'Content-Type': 'application/json',
                             'Authorization': 'Bearer '+self.dread.bearer_token,
                             'OrderId': str(self.dread.q_uuid)}

    def get_any_uuid(self):
        return requests.get(url=f"{self.dread.protocol}://{self.dread.host}/?UUID={self.dread.q_uuid}")

    def get_any_bearer(self):
        return requests.get(url=f"{self.dread.protocol}://{self.dread.host}/bearer",
                            headers=self.headers_bearer)

    def post_any_post(self):
        return requests.post(url=f"{self.dread.protocol}://{self.dread.host}/post",
                            headers=self.headers_post)
