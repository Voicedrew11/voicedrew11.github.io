import sys
import os
import tempfile
from subprocess import call
import time
import random

EDITOR = os.environ.get('EDITOR', 'nvim')

with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
    tf.flush()
    call([EDITOR, tf.name])

    title_bytes = tf.read().strip()
    title = title_bytes.decode('utf-8')

with tempfile.NamedTemporaryFile(suffix=".tmp") as af:
    af.flush()
    call([EDITOR, af.name])

    contents_bytes = af.read().strip()
    contents = contents_bytes.decode('utf-8')

time_format = "%Y-%m-%d %H:%M:%S"
date = time.strftime("%Y-%m-%d", time.gmtime(time.time() - 5 * 3600))
time = time.strftime("%H:%M:%S", time.gmtime(time.time() - 5 * 3600))

final = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="index.css">
</head>

<header>
   <a href="../index.html">Home</a> 
   <a href="../articles/index.html">Blog</a> 
   <a href="feed.rss">Subscribe</a> 
</header>


<body>
    <h1>{title}</h1>
    <hr>
    <p>{contents}</p>
    <small>Published on {date} at {time}</small>
</body>
</html>
"""
random_number = random.randint(1000, 9999)
filename = title.replace(" ","-")
output_file = f"{filename}-{random_number}.html"

with open(output_file, "w") as file:
    file.write(final)

print(output_file)
