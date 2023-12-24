import json

import requests
from base.components.payload_api import PayloadAPI


class ClientAPI:
    def __init__(self, url, context):
        self.options = context
        self.url = url

    def get_request(self):
        param = self.options.param
        header_content = self.options.header
        response = requests.get(self.url, headers=header_content, params=param)
        return response

    def post_request(self):
        param = self.options.param
        header_content = self.options.header
        payload = json.dumps(PayloadAPI(self.options.file_name).read_payload_file())
        response = requests.post(self.url, headers=header_content, params=param, data=payload)
        return response

    def patch_request(self):
        header_content = self.options.header
        payload = json.dumps(PayloadAPI(self.options.file_name).read_payload_file())
        requests.post(self.url, headers=header_content, data=payload)

    def put_request(self):
        header_content = self.options.header
        requests.put(self.url, headers=header_content)

    def delete_request(self):
        gist_id = self.get_gist_id_from_file()
        header_content = self.options.header
        delete_url = f'{self.url}{gist_id}'
        response = requests.delete(delete_url, headers=header_content)
        return response

    def get_gist_id_from_file(self):
        with open('data/gist_id.json', 'r') as json_file:
            json_data = json.load(json_file)
        gist_id = list(json_data.values())[-1]
        return gist_id
