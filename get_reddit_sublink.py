import lxml.html
import urllib.request


# specify url
url = 'https://www.reddit.com/r/mexico/'


def getSubLinks(url):
    sublinks = []
    connection = urllib.request.urlopen(url)
    dom = lxml.html.fromstring(connection.read())
    for link in dom.xpath('//a/@href'):
        if not link.startswith('http'):
            sublinks.append('https://www.reddit.com'+link)
        else:
            sublinks.append(link)
    return sublinks

s = getSubLinks(url)

# filter out links with reddit comments
g = []
for link in s:
    if ('comments' in link) & (url in link):
            g.append(link)

# drop duplicates
f = list(set(g))

# print
i = 1
for link in f:
     print('reddit',i,': ',link)
     i += 1
