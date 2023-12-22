import requests


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
        requests.post(url, headers=header_content, params=parameters, data=payload)

    def patch_request(self):
        requests.post(url, headers=header_content, data=payload)

    def put_request(self):
        requests.put(url, headers=header_content)

    def delete_request(self, url):
        requests.delete(url, headers=header_content)
