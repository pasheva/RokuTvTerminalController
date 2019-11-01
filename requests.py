from requests import *

def keypress(url, key):
    request_url = url + '/keypress/' + key
    requests.post(request_url)

keypress('http://192.168.0.8:8060', 'select')