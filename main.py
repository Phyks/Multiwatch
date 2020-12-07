#!/usr/bin/env python3
import sys

import requests

from urllib.parse import urlencode

LOCALES = {
    'fr_FR': 'France',
    'en_AU': 'Australia',
    'en_CA': 'Canada',
    'de_DE': 'Germany',
    'pl_PL': 'Poland',
    'en_SG': 'Singapore',
    'en_UK': 'United Kingdom',
}

query = input('Movie/Show title? ')

req = requests.get(
    'https://apis.justwatch.com/content/titles/fr_FR/popular',
    params={
        'language': 'fr',
        'body': '{"page_size":5,"page":1,"query":"%s","content_types":["show","movie"]}' % query
    }
)

i = 0
list = []

if not 'items' in req.json() or not req.json()['items']:
    print('NOT FOUND')
    sys.exit()

for item in req.json()['items']:
    list.append(item['id'])
    print('%s. %s' % (i, item['title']))
    i += 1

print()
title_nb = None
while title_nb not in range(len(list)):
    title_nb = input('Choice? ')
    try:
        title_nb = int(title_nb)
    except ValueError:
        pass
print()

print('Available from these flatrate services:')
for locale, locale_name in LOCALES.items():
    print('> %s:' % locale_name)
    req = requests.get(
        'https://apis.justwatch.com/content/titles/show/%s/locale/%s?language=fr'
        % (list[title_nb], locale)
    )
    offers = {}
    if not req.json().get('offers', []):
        print('  None')
        continue

    for offer in req.json().get('offers', []):
        if offer['monetization_type'] != 'flatrate':
            continue
        offers[offer['urls']['standard_web']] = {}

    for url, offer in offers.items():
        print('  * %s' % url)
    print()