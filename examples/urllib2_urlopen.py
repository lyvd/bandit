from urllib2 import Request, urlopen
headers = {}
req = Request(headers=headers)
data = urlopen(req)
