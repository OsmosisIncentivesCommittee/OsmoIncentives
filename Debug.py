import urllib.request
import http.client

http.client.HTTPConnection.debuglevel = 1

response = urllib.request.urlopen('https://api-osmosis.imperator.co/tokens/v2/all')
