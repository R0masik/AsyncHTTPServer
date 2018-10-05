"""Client Test"""

import requests

if __name__ == "__main__":
    host = 'http://127.0.0.1:8888/'
    resp = requests.get(host)
    print(resp.json())
