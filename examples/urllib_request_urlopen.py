from urllib.request import urlopen, Request
data = urlopen(req,timeout=10,context=ctx).read().decode('utf-8')
