import json

from behave import *
from base.components.client_api import ClientAPI
from base.components.response_api import ResponseAPI
from base.components.payload_api import PayloadAPI
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
            context.response = ClientAPI(url, context).post_request()
        case 'patch':
            pass
        case 'delete':
            context.response = ClientAPI(url, context).delete_request()
        case _:
            pass

    with open('response_json', 'w', encoding="utf-8") as write_file:
        try:
            json.dump(context.response.json(), write_file)
        except:
            json.dump("{}", write_file)


@step("Load payload from {file_name} file")
@step("Load payload from {file_name} file with updated values")
def load_payload(context, file_name, values=None):
    """ load a payload with the option of updating it by JSONPath
    :param context:
    :param file_name:
    :param values: str
    """

    context.json_path_value = to_flat_dict(context)
    full_file_name = 'data/payloads/' + file_name
    context.file_name = full_file_name

    for path in context.json_path_value:
        PayloadAPI(full_file_name).replace_payload(path, context.json_path_value[path])


@step("Verify response value")
def verify_response(context):
    """verify the response values"""
    values_to_varify = to_flat_dict(context)

    for key in values_to_varify:
        match key:
            case 'status code':
                ResponseAPI(context).verify_response_status_code(values_to_varify['status code'])
            case 'name':
                ResponseAPI(context).verify_contains(JsonLocators.owners_logins, values_to_varify['name'])
            case 'No of Repos':
                ResponseAPI(context).verify_length(JsonLocators.number_of_repos, values_to_varify['No of Repos'])


@step("Save gist id")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ResponseAPI(context).get_gist_id_from_response()
