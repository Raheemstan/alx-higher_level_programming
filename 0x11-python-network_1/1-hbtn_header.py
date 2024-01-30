import urllib.request
import sys

def get_x_request_id(url):
    """Sends a request to the URL and returns the value of the X-Request-Id variable found in the header of the response"""
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        return x_request_id

if __name__ == "__main__":
    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
    print(x_request_id)
