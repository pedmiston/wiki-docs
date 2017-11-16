#!/usr/bin/env python
# Usage: load_article_stats.py [article name]
# Returns: facts about the article in json
import sys
import json
import pywikibot
from datetime import datetime
site = pywikibot.Site('en', 'wikipedia')
page = pywikibot.Page(site, sys.argv[1])
section_headers = [line for line in page.text.splitlines()
                   if line.startswith('== ')]
age_seconds = (datetime.now() - page.oldest_revision['timestamp']).total_seconds()
data = dict(
    n_edits = page.revision_count(),
    n_authors = len(page.contributors()),
    n_sections = len(section_headers),
    age_days = age_seconds/(60 * 60 * 24)
)
print(json.dumps(data))
