import os
import requests
from dotenv import load_dotenv
import hmac
import time
import hashlib
from urllib.parse import urlencode, urljoin
from contextlib import contextmanager

load_dotenv(os.path.join(os.path.dirname(__file__), '..', os.environ.get('ENV', 'local')+'.env'))

# must define following env variable to run
BINANCE_API_KEY = os.environ.get('binance-api-key')
BINANCE_API_SECRET = os.environ.get('binance-api-secret')
BASE_URL = urljoin(os.environ.get('BINANCE_API_URL', 'https://testnet.binance.vision'),
                        os.environ.get('BINANCE_API_ENDPOINT'))

def hashing(query_string):
    return hmac.new(BINANCE_API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def get_timestamp():
    return int(time.time() * 1000)

@contextmanager
def Session():
    try:
        session = requests.Session()
        session.headers.update({
            'Content-Type': 'application/json;charset=utf-8',
            'X-MBX-APIKEY': BINANCE_API_KEY
        })
        yield session
    finally:
        session.close()

# used for sending request requires the signature
def send_signed_request(http_method, url_path, payload={}):
    query_string = urlencode(payload, True)
    if query_string:
        query_string = f"{query_string}&timestamp={get_timestamp()}"
    else:
        query_string = f'timestamp={get_timestamp()}'

    url = BASE_URL + url_path + '?' + query_string + '&signature=' + hashing(query_string)
    print(f"{http_method} {url}")
    params = {'url': url, 'params': {}}
    with Session() as sess:
        response = getattr(sess, http_method)(**params)
    return response.json()

# used for sending public data request
# public requests are only GET
def send_public_request(url_path, payload={}):
    url = BASE_URL + url_path
    print(f"{url}")
    with Session() as sess:
        response = sess.get(url=url, params=payload)
    return response.json()