import feedparser

def parse_feed():
    url = "http://feeds.bbci.co.uk/news/world/rss.xml"
    feed = feedparser.parse(url)

    print("Title: ", feed.feed.title)                   # Print the feed title
    print("Description: ", feed.feed.description)       # Print the feed description

    for entry in feed.entries:
        print(entry.title)          # Print the title of each entry
        print(entry.link)           # Print the link of each entry
        print(entry.summary)        # Print the summary of each entry
        print(entry.published)      # Print the published date of each entry

parse_feed()
