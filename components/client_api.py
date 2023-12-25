import json

import requests
from base.components.payload_api import PayloadAPI
from components.git_token_and_user import GitToken


class ClientAPI:
    def __init__(self, url, context):
        self.options = context
        self.url = url

    def get_request(self):
        param = self.options.param
        header_content = self.options.header
        if self.url.find('{owner}') == -1:
            res_url = self.url
        else:
            res_url = self.url.format(owner=GitToken.git_owner, repo=GitToken.git_repo)
        response = requests.get(res_url, headers=header_content, params=param)
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
        if self.url.find('{owner}') == -1:
            res_url = self.url
        else:
            res_url = self.url.format(owner=GitToken.git_owner, repo=GitToken.git_repo)
        response = requests.patch(res_url, headers=header_content, data=payload)
        return response

    def put_request(self):
        header_content = self.options.header
        requests.put(self.url, headers=header_content)

    def delete_gist_request(self):
        gist_id = self.get_gist_id_from_file()
        header_content = self.options.header
        delete_url = f'{self.url}{gist_id}'
        response = requests.delete(delete_url, headers=header_content)
        return response

    def delete_repo_request(self):
        header_content = self.options.header
        if self.url.find('{owner}') == -1:
            delete_url = self.url
        else:
            delete_url = self.url.format(owner=GitToken.git_owner, repo=GitToken.git_repo)
        response = requests.delete(delete_url, headers=header_content)
        return response

    def get_gist_id_from_file(self):
        with open('data/gist_id.json', 'r') as json_file:
            json_data = json.load(json_file)
        gist_id = list(json_data.values())[-1]
        return gist_id
