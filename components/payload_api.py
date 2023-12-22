import json
import jsonpath_ng


class PayloadAPI:

    def read_payload_file(self, file_name):
        with open(file_name, 'r') as file:
            file_data = file.read()
        payload = json.dumps(file_data)
        return payload

    def add_payload(self, file_name, value, path):
        data_ = ''
        with open(file_name, 'a', encoding="utf-8") as append_file:
            append_file.write(data_)

    def delete_payload(self, key, path):
        pass

    def replace_payload(self, key, path):
        pass

