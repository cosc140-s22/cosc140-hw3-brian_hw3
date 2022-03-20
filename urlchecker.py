#######################################################
#
# COSC 140 Homework 3: URL checker
#
#######################################################

def urlchecker(url):
  if url.count(" ")>0:
    return False
  if url.count("#")>0 and url.count("?")>0:
    if url.find("#") > url.find("?"):
      return False
  if url.count("#")>1 or url.count("?")>1:
    return False
  before, after = url.split("://")
  if before != "http" and before != "https":
    return False
  if after.count(":")>1:
    return False
  if after.count(":")==1:
    if after.find(":")==0:
      return False
    hostname, rest = after.split(":")
    if rest.count("/")==0:
      return False
    portid, rest = rest.split("/")
    return portid.isdigit()
  if after.count("/")==0:
    return False
  if after.find("/")==0:
    return False
  return True
#print(urlchecker('https://example/?:3000#'))
def testurl():
    urls = [ # valid
      ['https://example.com/', True],
      ['http://example.com/', True],
      ['http://example.com/?query', True],
      ['http://example.com/#fragment', True],
      ['http://example/', True],
      ['http://example/path/', True],
      ['http://example/path', True],
      ['https://example.com:3000/path#fragment?query', True],
      ['https://example.com/path#fragment?query', True],
      # invalid
      ['htt://example/', False],
      ['httpss://example/', False],
      ['https://example/:3000', False],
      ['https://example/?:3000?', False],
      ['https://example/?:3000#', False],
      ['https://example/xy z', False],
      ['https://example/xyz:', False],
      ['https://example', False],
    ]
    for url,expected in urls:
        if urlchecker(url) != expected:
            print(f"{url} is not valid, but your function claimed the opposite")
        else:
            print(f"{url} - ok")
