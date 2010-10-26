#!/usr/bin/env python
# Written by Nick Welch in 2010.
# No copyright.  This work is dedicated to the public domain.
# For full details, see http://creativecommons.org/publicdomain/zero/1.0/

import sys, csv, urllib, urllib2, time

from lxml.html import fromstring

reader = csv.reader(file(sys.argv[1]))

artist_names = [ row[0].strip() for row in reader if row and row[0].strip() ]

results_by_artist = []

for artist in artist_names:
    print artist
    url = 'http://thepiratebay.org/search/{0}/0/7/100'.format(urllib.quote(artist))
    tree = fromstring(urllib2.urlopen(url).read())

    results = []

    for tr in tree.cssselect("table#searchResult > tr"):
        seeds = int(tr.getchildren()[2].text_content())
        if seeds == 0:
            continue

        url = tr.getchildren()[1].cssselect("a")[1].attrib['href']

        results.append((seeds, url))

    results.sort(reverse=True)

    results_by_artist.append((artist, results))

    time.sleep(2)


f = file('torrents.html', 'w')
f.write("""
<style>
    a:link, a:visited, a:hover, a:active { text-decoration: none; }
</style>
""")

for artist, results in results_by_artist:

    f.write('<h1>{0}</h1>'.format(artist))

    if results:
        f.write('<table>')
        f.write('<tr><th>torrent</th><th>seeds</th></tr>')
        for result in results:
            seeds, url = result
            filename = url.split('/')[-1].rsplit('.', 3)[0]

            f.write('<tr>')
            f.write('<td><a href="{0}">{1}</a></td>'.format(url, filename))
            f.write('<td>{0}</td>'.format(seeds))
            f.write('</tr>')
        f.write('</table>')
    else:
        f.write("<h4>sorry, didn't find anything.</h4>")

