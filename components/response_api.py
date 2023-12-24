import json
from jsonpath_ng import jsonpath, parse
import random


class ResponseAPI:
    def __init__(self, context):
        self.response = context.response

    def get_value_by_jsonpath(self, path):
        # JSONPath expression
        expression = parse(path)

        file_name = 'response_json'
        with open(file_name, 'r') as json_file:
            json_data = json.load(json_file)

        # Apply the expression to the JSON data
        value = [match.value for match in expression.find(json_data)]
        return value

    def verify_length(self, path, expected_length):
        actual_length = str(len(self.get_value_by_jsonpath(path)))
        assert expected_length == actual_length, (f'Item length does not match:'
                                                  f'\nExpected: {expected_length}'
                                                  f'\nActual:   {actual_length}')

    def verify_contains(self, path, expected_value):
        actual_value = self.get_value_by_jsonpath(path)

        if len(actual_value) == 1:
            actual_val = str(actual_value[0])
            assert expected_value in actual_val, (f'Response does not contain value:'
                                                  f'\nExpected: {expected_value}'
                                                  f'\nActual:   {actual_val}')
        else:
            assert expected_value in actual_value, (f'Response does not contain value:'
                                                    f'\nExpected: {expected_value}'
                                                    f'\nActual:   {actual_value}')

    def verify_equals(self, path):
        pass

    def verify_response_status_code(self, code):
        assert self.response.status_code == int(code), (f'Status code error:'
                                                        f'\nExpected: {code}'
                                                        f'\nActual:   {self.response.status_code}')

    def get_gist_id_from_response(self):
        gist_id = self.response.json()['id']
        print(gist_id)
        rnd_num = random.randrange(1, 1000)
        new_id = f'id_{rnd_num}'
        data_object = {new_id: gist_id}
        with open('data/gist_id.json', 'w') as json_file:
            json.dump(data_object, json_file)
