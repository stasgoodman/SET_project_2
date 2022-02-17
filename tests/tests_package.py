from tests.base import BaseTest


class Test1stBin(BaseTest):

    def setUp(self):
        super(Test1stBin, self).setUp()

    def test_1_step_1_status_200(self):
        """
        01.1 UUID + Status 200 =
        """
        self.assertEquals(self.gotobin.get_any_uuid().status_code, self.status, "FU1")

    def test_1_step_2_uuid_not_empty(self):
        """
        01.2 UUID response = UUID request -
        """
        req_uuid = str(self.gotobin.get_any_uuid().request.url.split("?UUID=")[-1])
        resp_uuid = str(self.gotobin.get_any_uuid().url.split("?UUID=")[-1])
        self.assertEquals(req_uuid, resp_uuid, "FU1")

    def test_2_step_1_bearer_status_200(self):
        """
        02.1 Bearer + status = 200
        """
        self.assertEquals(self.gotobin.get_any_bearer().status_code, self.status)

    def test_2_step_2_bearer_not_empty(self):
        """
        02.2 Bearer response equals Bearer request -
        """
        req_bearer = self.gotobin.get_any_bearer().request.headers.get("Authorization").split("Bearer ")[-1]
        resp_bearer = self.gotobin.get_any_bearer().json().get("token")
        self.assertEquals(req_bearer, resp_bearer, "FU1")

    def test_2_step_3_is_authed(self):
        """
        02.3 Authenticated = True
        """
        is_auth = self.gotobin.get_any_bearer().json().get("authenticated")
        self.assertTrue(is_auth is True, "FU2")

    def test_3_step_1_orderid_equals(self):
        """
        03.1 requested OrderId equals OrderId in response body
        """
        req_order_id = self.gotobin.post_any_post().request.headers.get("OrderId")
        resp_order_id = self.gotobin.post_any_post().json().get("headers").get("Orderid")
        self.assertTrue(req_order_id == resp_order_id, "FU2")

    def test_3_step_2_bearer_not_empty(self):
        """
        03.2 requested auth token matching response headers auth token
        """
        req_order_id = self.gotobin.post_any_post().request.headers.get("Authorization").split("Bearer ")[-1]
        resp_order_id = self.gotobin.post_any_post().json().get("headers").get("Authorization").split("Bearer ")[-1]
        self.assertTrue(req_order_id == resp_order_id, "FU2")
