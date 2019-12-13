"""Client Test"""

import requests

if __name__ == "__main__":
    host = 'http://localhost:3000'
    resp = requests.get(host)
    print(resp.json())
