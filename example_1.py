#!/usr/bin/env python

import urllib
from pprint import pprint
from HTMLTableParser import HTMLTableParser

# Create the parser
p = HTMLTableParser()

try:
    # Get tables from this webpage
    url = "http://www.franjeado.com/stats.php"
    req = urllib.urlopen(url)

    # Parse the data
    p.feed(req.read())

except Exception, e:
    print e

# Show results
pprint(p.tables)

