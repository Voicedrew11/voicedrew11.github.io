import argparse
import markdown2
import re
from datetime import datetime

# Create an argument parser
parser = argparse.ArgumentParser(description='Generate a microblog from a Markdown file and insert it under <!--insert_here--> in index.html.')

# Add a positional argument for the Markdown file
parser.add_argument('markdown_file', help='Path to the Markdown file')

# Parse the command-line arguments
args = parser.parse_args()

# Read the Markdown file
with open(args.markdown_file, 'r') as md_file:
    markdown_content = md_file.read()

# Convert Markdown to HTML
html_content = markdown2.markdown(markdown_content)

# Extract the first line of the Markdown content
first_line = markdown_content.split('\n', 1)[0]

# Sanitize the first line to create a valid ID (remove spaces and special characters)
id_from_first_line = re.sub(r'[^a-zA-Z0-9_-]', '', first_line.lower())

# Create the HTML content with the <article> tag and the ID
article_html = f'<article id="{id_from_first_line}">{html_content}<p class="timestamp">Posted on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p></article>'

# Read the existing 'index.html' file
with open('index.html', 'r') as html_file:
    existing_html = html_file.read()

# Define the placeholder where you want to insert the HTML
placeholder = '<!--insert_here-->'

# Split the HTML content using the placeholder
parts = existing_html.split(placeholder, 1)

# Check if the placeholder was found
if len(parts) > 1:
    # Insert the HTML content after the placeholder with two line breaks
    modified_html = parts[0] + placeholder + '\n\n' + article_html + parts[1]
    
    # Save the modified HTML back to 'index.html'
    with open('index.html', 'w') as html_file:
        html_file.write(modified_html)

    print(f'Content from {args.markdown_file} has been inserted under <!--insert_here--> in index.html with ID: {id_from_first_line}')
else:
    print(f'Error: <!--insert_here--> not found in index.html.')
