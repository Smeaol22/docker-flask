from requests import RequestException, get, post

from docker_flask.docker.conf import BASE_CONTAINER_ADDRESS, EXPOSE_PORT


class BaseClient:
    def __init__(self):
        self.base_url = BASE_CONTAINER_ADDRESS
        self.port = EXPOSE_PORT

    def get(self, url_last_digit, endpoints_path="", path_params="", query_params={}):
        response = get(f'http://{self.base_url}.{url_last_digit}:{self.port}/{endpoints_path}{path_params}',
                       params=query_params)
        if response.status_code >= 500:
            raise DockerException(response=response, requests=response.request)
        if response.status_code >= 400:
            raise BadRequestException(response=response, requests=response.request)
        return response

    def post(self, url_last_digit, endpoints_path="", params={}):
        response = post(f'http://{self.base_url}.{url_last_digit}:{self.port}/{endpoints_path}', params=params)
        if response.status_code >= 500:
            raise DockerException(response=response, requests=response.request)
        if response.status_code >= 400:
            raise BadRequestException(response=response, requests=response.request)
        return response


class BadRequestException(RequestException):
    """ The request is false"""


class DockerException(RequestException):
    """ Failed to communicate with docker"""
