import json

from behave import *
from base.components.client_api import ClientAPI
from base.components.response_api import ResponseAPI
from base.components.helpers import *
from components.git_token import GitToken
from components.json_locators import JsonLocators


# @step("Send {request_method} request to {url}")
@step("Send {request_method} request to {url}")
@step("Send {request_method} request with authentication to {url}")
def send_request(context, request_method, url):
    """ handle any request
    :param context:
    :param request_method:
    :type url: str
    :param: request_method: str
    """

    context.param = to_flat_dict(context)
    token = f'token {GitToken.git_token}'
    context.header = {'Authorization': token}

    match request_method.lower():
        case 'get':
            context.response = ClientAPI(url, context).get_request()
        case 'post':
            pass
        case 'patch':
             pass
        case 'delete':
            pass
        case _:
            pass

    with open('response_json', 'w', encoding="utf-8") as write_file:
        json.dump(context.response.json(),write_file)

@step("Load payload from {file_name} file")
@step("Load payload from {file_name} file with updated values")
def load_payload(context, file_name, values = None):
    """ load a payload with the option of updating it by JSONPath
    :param context:
    :param file_name:
    :param values: str
    """
    pass


@step("Verify response value")
def verify_response(context):
    """verify the response values"""
    print(to_flat_dict(context))
    values_to_varify = to_flat_dict(context)
    status_code_expected = int(values_to_varify['status code'])

    ResponseAPI(context).verify_response_status_code(status_code_expected)
    ResponseAPI(context).verify_contains(JsonLocators.owners_logins, values_to_varify['name'])
    ResponseAPI(context).verify_contains(JsonLocators.number_of_repos, values_to_varify['No of Repos'])
