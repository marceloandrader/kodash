#!/usr/local/bin/python

# modified from https://github.com/datasaur/pgdash/blob/master/pgdoc2set.py

import os, re, sqlite3, string
from bs4 import BeautifulSoup, NavigableString, Tag 

db = sqlite3.connect('KnockoutJS.docset/Contents/Resources/docSet.dsidx')
cur = db.cursor()

try: cur.execute('DROP TABLE searchIndex;')
except: pass
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = 'KnockoutJS.docset/Contents/Resources/Documents'

page = open(os.path.join(docpath,'documentation/introduction.html')).read()
soup = BeautifulSoup(page)

any = re.compile('.*')
for tag in soup.find_all('a', {'href':any}):
    name = tag.text.strip()
    if len(name) > 0:
        path = tag.attrs['href'].strip()
        path = string.replace(path, '../documentation/', 'documentation/')
        cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'func', path))
        # print 'name: %s, path: %s' % (name, path)

db.commit()
db.close()
print 'Index has been generated'
