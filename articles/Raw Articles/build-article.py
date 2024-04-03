import markdown
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python build-article.py input.md")


input_file = sys.argv[1] 
try:
    with open(input_file, "r") as file:
        markdown_text = file.read()

    output_file = os.path.splitext(input_file)[0] + ".html"

    html = markdown.markdown(markdown_text)

    lines = markdown_text.split('\n')
    if lines:
        first_line = lines[0].lstrip('# ').strip() 
    else:
        first_line = "No content in the Markdown file."

    final_html = f"""
<!DOCTYPE html>
<html lang="">

<head>
	<meta charset="utf-8">
	<title>{first_line}</title>
	<link rel="stylesheet" href="../gbl.css">
</head>

<nav>
  <a href="/index.html">/About</a>
  <a href="/articles/">/Blog</a>
  <a href="/bookshelf">/Bookshelf</a>
  <a href="/microblog/">/Microblog</a>
  <a href="/links.html">/Links</a>
</nav>

	<body>
        <article>
            {html}
        </article>
	</body>
</html>
"""

    with open(output_file, "w") as file:
        file.write(final_html)

    print(f"HTML content written to '{output_file}'.")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
