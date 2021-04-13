import requests

try:
    r = requests.get('https://httpbin.org/delay/6', timeout=3)
    print(r)

# TODO: get this right!
# https://docs.python-requests.org/en/master/_modules/requests/exceptions/

except requests.exceptions.RequestException():
    print("There was an ambiguous except that occurred.")

except requests.exceptions.ConnectionError():
    print("A Connection error occurred.")

except requests.exceptions.HTTPError():
    print("An HTTP error occurred.")

except requests.exceptions.URLRequired():
    print("A valid URL is required to make a request.")

except requests.exceptions.TooManyRedirects():
    print("Too many redirects.")

except requests.exceptions.ConnectTimeout():
    print("The request timed out while trying to connect.")

# Requests that produced this error are safe to retry.

except requests.exceptions.ReadTimeout():
    print("The server did not send any data in the allotted amount of time.")

except requests.exceptions.Timeout():
    print("The request timed out.")

# Catching this error will catch both ConnectTimeout and ReadTimeout errors.
