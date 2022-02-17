from tests.base import BaseTest
import re


class Test1stBin(BaseTest):

    def setUp(self):
        super(Test1stBin, self).setUp()

    def test_1_step_1_status_200(self):
        """
        01.
        """
        self.assertEquals(self.gotobin.get_any().status_code, self.status, "FU1")

    def test_1_step_2_uuid_not_empty(self):
        """
        01.
        """
        req_uuid = str(self.gotobin.get_any().request.url.split("?UUID=")[-1])
        resp_uuid = str(self.gotobin.get_any().url.split("?UUID=")[-1])
        self.assertEquals(req_uuid, resp_uuid, "FU1")
