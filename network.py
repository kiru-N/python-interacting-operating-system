import requests
import socket


def check_localhost():
    local_host = socket.gethostbyname('localhost')
    return local_host == "127.0.0.1"


def check_connectivity():
    request = requests.get('http://www.google.com')
    if str(request.status_code).isnumeric():
        return request.status_code == 200
