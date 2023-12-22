import json
from jsonpath_ng import jsonpath, parse


class ResponseAPI:
    def __init__(self, context):
        self.response = context.response

    def verify_length(self, path):
        pass

    def verify_contains(self, path, expected_value):
        # JSONPath expression
        expression = parse(path)

        file_name = 'response_json'
        with open(file_name, 'r') as json_file:
            json_data = json.load(json_file)

        # Apply the expression to the JSON data
        actual_value = [match.value for match in expression.find(json_data)]

        if len(actual_value) == 1:
            actual_val = str(actual_value[0])
            assert expected_value == actual_val, (f'Response does not contain value:'
                                                  f'\nExpected: {expected_value}'
                                                  f'\nActual:   {actual_val}')
        else:
            assert expected_value in actual_value, (f'Response does not contain value:'
                                                    f'\nExpected: {expected_value}'
                                                    f'\nActual:   {actual_value}')

    def verify_equals(self, path):
        pass

    def verify_response_status_code(self, code):
        assert self.response.status_code == code, (f'Status code error:'
                                                   f'\nExpected: {code}'
                                                   f'\nActual:   {self.response.status_code}')
