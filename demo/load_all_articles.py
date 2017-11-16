#!/usr/bin/env python
# Load article stats from file.
import sys
import json
import pywikibot
import pandas
from datetime import datetime

site = pywikibot.Site('en', 'wikipedia')

def get_article_stats(name):
    page = pywikibot.Page(site, name)
    section_headers = [line for line in page.text.splitlines()
                       if line.startswith('== ')]
    age_seconds = (datetime.now() - page.oldest_revision['timestamp']).total_seconds()
    data = dict(
        name = name,
        n_edits = page.revision_count(),
        n_authors = len(page.contributors()),
        n_sections = len(section_headers),
        age_days = age_seconds/(60 * 60 * 24)
    )
    return data

if __name__ == '__main__':
    articles = []
    for name in open(sys.argv[1]):
        try:
            data = get_article_stats(name)
        except:
            sys.stderr.write(f'Error in getting article "{name}"')
        else:
            articles.append(data)

    pandas.DataFrame(articles).to_csv(sys.stdout, index=False)
