import requests
from utils.configs_reader import DataReader


class GotoBin:

    def __init__(self):
        self.dread = DataReader()

    def get_any(self):
        return requests.get(url=f"{self.dread.protocol}://{self.dread.host}/?UUID={self.dread.uuid}")
