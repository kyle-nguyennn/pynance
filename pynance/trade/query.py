from pynance import send_signed_request
from pynance.model.enums import HttpMethod


def getAccountInfo():
    path = 'account'
    resp = send_signed_request(HttpMethod.GET.value, path)
    return resp