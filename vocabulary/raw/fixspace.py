import os
from bs4 import BeautifulSoup, Comment

# Directory containing the HTML files
directory = r'C:\Users\pc\pyprojects\KanjiList\kanjilist-live\vocabulary'

# Function to compact HTML content
def compact_html_file(file_path):

   
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove comments
    for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Minify the HTML by removing unnecessary whitespace and line breaks
    compact_html = soup.prettify(formatter=None)
    compact_html = compact_html.replace('\n', '').replace('  ', '')

    # Write the compacted HTML back to the file or a new file
    compacted_file_path = file_path.replace('.html', '.html')
    with open(compacted_file_path, 'w', encoding='utf-8') as file:
        file.write(compact_html)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        file_path = os.path.join(directory, filename)
        compact_html_file(file_path)
        print(f"Processed {filename}")
