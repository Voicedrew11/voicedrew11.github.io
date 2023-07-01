import markdown
from feedgen.feed import FeedGenerator

# Function to extract Markdown headings as RSS items
def extract_headings_as_items(md_content):
    headings = md_content.split('\n# ')[1:]
    items = []
    for heading in headings:
        title, _, description = heading.partition('\n')
        link = '#' + title.lower().replace(' ', '-')
        items.append((title, link, description))
    return items

# Read the input Markdown file
input_file = "journal.md"
with open(input_file, 'r') as file:
    md_content = file.read()

# Convert Markdown to HTML
html_content = markdown.markdown(md_content)

# Extract Markdown headings as RSS items
items = extract_headings_as_items(md_content)

# Generate the RSS feed
fg = FeedGenerator()
fg.title('st.ream')
fg.link(href='https://voicedrew.xyz/steam/stream.html', rel='alternate')
fg.description('Literal st.ream of conciousnes.')

for item in items:
    fe = fg.add_entry()
    fe.title(item[0])
    fe.link(href=item[1])
    fe.description(item[2])

# Save the RSS feed to a file
output_file = "feed.xml"
fg.rss_file(output_file)

print("RSS feed generated successfully. Output file:", output_file)
