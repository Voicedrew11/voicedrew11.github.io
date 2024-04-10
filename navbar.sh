#!/bin/bash

#!/bin/bash

# Define custom navigation content
custom_content='<nav>\
  <a href="/index.html"><img class="icon" src="/images/index.png"></a>\
  <a href="/articles/"><img class="icon" src="/images/note.png"></a>\
  <a href="/bookshelf"><img class="icon" src="/images/about.png"></a>\
  <a href="/microblog/"><img class="icon" src="/images/microblog.png"></a>\
  <a href="/links.html"><img class="icon" src="/images/links.png"></a>\
</nav>'

# Function to recursively find HTML files in a directory
find_html_files() {
    local directory="$1"
    local pattern="$2"

    find "$directory" -type f -name "$pattern"
}

# Function to replace content within <nav></nav> tags
replace_nav_content() {
    local file="$1"
    local content="$2"

    # Replace content within <nav></nav> tags
    sed -i -e "/<nav>/,/<\/nav>/c\\
$content
" "$file"
}

# Main script
main() {
    local directory="${1:-.}"  # Default to current directory if not provided
    local pattern="*.html"

    # Find HTML files recursively
    while IFS= read -r file; do
        # Replace content within <nav></nav> tags
        replace_nav_content "$file" "$custom_content"
        echo "Content replaced in: $file"
    done < <(find_html_files "$directory" "$pattern")
}

# Call the main function with the working directory as the argument
main "$(pwd)"

cho "Replacement process completed."
