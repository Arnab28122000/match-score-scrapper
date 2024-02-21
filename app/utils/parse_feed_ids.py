import re

def extract_feed_ids(data):
    pattern = r'AA÷(.*?)¬'
    feed_ids = re.findall(pattern, data)
    return feed_ids
