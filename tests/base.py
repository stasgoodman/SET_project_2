import json
import unittest
import random
import string
# from collections import counter
from utils.httpbin_requests import GotoBin


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gotobin = GotoBin()
        cls.status = 200

    def setUp(self):
        pass
