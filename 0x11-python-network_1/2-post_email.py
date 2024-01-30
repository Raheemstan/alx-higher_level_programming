import urllib.request
import urllib.parse
import sys

def post_email(url, email):
    """Sends a POST request to the specified URL with the email as a parameter,
    and returns the body of the response"""
    value = {'email': email}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8", "replace")

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = post_email(url, email)
    print(response_body)
