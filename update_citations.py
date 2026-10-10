import yaml
from scholarly import scholarly

# Fetch your profile data
author = scholarly.search_author_id('fqDMcoMAAAAJ')
scholarly.fill(author, sections=['indices'])

# Extract total citations
data = {'total_citations': author['citedby']}

# Write to the Jekyll data file
with open('_data/metrics.yml', 'w') as f:
    yaml.dump(data, f)
