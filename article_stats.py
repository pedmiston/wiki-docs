#!/usr/bin/env python
# Usage: article_stats.py [article_name]
import sys
import json
import pywikibot
site = pywikibot.Site('en', 'wikipedia')
page = pywikibot.Page(site, sys.argv[1])
section_headers = [line for line in page.text.splitlines()
                   if line.startswith('== ')]
data = dict(
    n_revisions = page.revision_count(),
    n_contributors = len(page.contributors()),
    n_sections = len(section_headers)
)
print(json.dumps(data))
