from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator

# Step 1: Read the HTML file
try:
    with open("index.html", "r") as file:
        html_data = file.read()
except FileNotFoundError:
    print("HTML file not found. Please check the file path.")
    exit(1)

# Step 2: Parse the HTML
try:
    soup = BeautifulSoup(html_data, 'html.parser')
except Exception as e:
    print("Error occurred while parsing HTML:", str(e))
    exit(1)

# Step 3: Find the first article tag
try:
    article_tag = soup.find('article')
    if article_tag is None:
        raise ValueError("Article tag not found")
except ValueError as e:
    print(str(e))
    exit(1)

# Step 4: Extract relevant information
try:
    title_element = article_tag.find('h1')
    description_element = article_tag.find('p')
    link_element = article_tag.find('a')
    if title_element is None or description_element is None or link_element is None:
        raise ValueError("Required child element(s) not found")
    
    title = title_element.text
    description = description_element.text.strip()
    link = link_element['href']
except ValueError as e:
    print(str(e))
    exit(1)
except Exception as e:
    print("Error occurred while extracting information:", str(e))
    exit(1)

# Step 5: Create the RSS element
fg = FeedGenerator()
fg.id(link)
fg.title(title)
fg.description(description)
fg.link(href=link)

# Step 6: Add any additional information to the RSS element

# Step 7: Generate the RSS feed
rss_string = fg.rss_str(pretty=True)

# Step 8: Save the RSS feed to a file
try:
    with open("output.xml", "w") as file:
        file.write(rss_string)
    print("RSS feed created successfully.")
except Exception as e:
    print("Error occurred while saving the RSS feed:", str(e))
    exit(1)
