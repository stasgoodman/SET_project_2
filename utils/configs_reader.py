import json
import uuid

json_file_path = ".\configs\data.json"


def open_json_data():
    with open(json_file_path, "r") as f:
        json_data = json.load(f)
    return json_data


class DataReader:

    def __init__(self):
        test_data = open_json_data()
        self.protocol = test_data["protocol"]
        self.host = test_data["host"]
        self.q_uuid = uuid.uuid1()
        self.q_bearer = test_data["authorization"]["bearer"]
        self.bearer_token = test_data["authorization"]["bearer_token"]
