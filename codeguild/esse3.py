import requests
import json
import base64
from flask import session

URL_API = "https://uniparthenope.esse3.cineca.it/e3rest/api"


def sendRequest(tok, url):
    headers = {'Authorization': 'Basic %s' % tok}
    response = requests.get(url, headers=headers)
    response = response.text
    response = json.loads(response)
    return response


def login(username, password):
    url = URL_API + "/login"

    token = username + ":" + password
    token = base64.b64encode(bytes(token, 'utf-8'))
    token = token.decode("utf-8")

    headers = {'Authorization': 'Basic %s' % token}

    response = sendRequest(token, url)

    if 'errDetails' in response:
        return False

    session['username'] = username
    session['authToken'] = token
    session['jsessionId'] = response['authToken']
    session['userFirstName'] = response['user']['firstName'].capitalize()
    session['userLastSurname'] = response['user']['lastName'].capitalize()
    session['cdsId'] = response['user']['trattiCarriera'][0]['cdsId']
    session['userMatId'] = response['user']['trattiCarriera'][0]['matId']
    session['mat'] = response['user']['trattiCarriera'][0]['matricola']

    return response











