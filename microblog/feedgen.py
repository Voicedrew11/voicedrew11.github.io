import feedparser
from bs4 import BeautifulSoup
from datetime import datetime

# Create an RSS feed
feed = {
    'title': 'Article RSS Feed',
    'link': 'https://example.com',
    'description': 'RSS feed generated from article tags in an HTML document',
    'items': []
}

# Read HTML content from the 'index.html' file
with open('index.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all article tags in the HTML
article_tags = soup.find_all('article')

for article in article_tags:
    # Extract the title and content from each article
    title = article.find('h2').text.strip()
    content = article.find('div', class_='content').text.strip()

    # Create a new RSS item for each article
    item = {
        'title': title,
        'description': content,
        'pubDate': datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z'),
    }

    # Add the item to the feed
    feed['items'].append(item)

# Generate the RSS feed as a string
rss_feed = f'''<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
    <title>{feed['title']}</title>
    <link>{feed['link']}</link>
    <description>{feed['description']}</description>
    <pubDate>{datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate>
    {"".join([f'''
    <item>
        <title>{item['title']}</title>
        <description>{item['description']}</description>
        <pubDate>{item['pubDate']}</pubDate>
    </item>''' for item in feed['items']])}
</channel>
</rss>
'''

# Save the RSS feed to a file
with open('article_feed.xml', 'w', encoding='utf-8') as rss_file:
    rss_file.write(rss_feed)

print('RSS feed generated and saved as article_feed.xml')
