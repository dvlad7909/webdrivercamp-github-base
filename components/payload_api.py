import json
import jsonpath_ng
from jsonpath_ng import jsonpath, parse


class PayloadAPI:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_payload_file(self):
        with open(self.file_name, 'r') as file:
            payload = json.load(file)
        return payload

    def write_json_file(self, json_data):
        with open(self.file_name, 'w') as file:
            json.dump(json_data, file)

    def add_payload(self, path, value):
        pass

    def delete_payload(self, path):
        pass

    def replace_payload(self, path, value):
        # Parse JSONPath expression
        expression = parse(path)

        # Read JSON data from file
        json_data = self.read_payload_file()

        # Find all matches
        matches = [match for match in expression.find(json_data)]

        # Replace each match with the new value in the original JSON data
        for match in matches:
            # Get the path of the match
            path_new = match.full_path
            # Update the original JSON data with the new value at the path
            json_data[str(path_new)] = value

        # Write updated JSON data to file

        self.write_json_file(json_data)

        # self.write_json_file(json_data)
