import pandas as pd
import os
from bs4 import BeautifulSoup


#import xlsx file
_10kwords = pd.read_excel('raw/10Kwords.xlsx') 
_6kwords = pd.read_excel('raw/6Kwords.xlsx') 

#eliminate THE LAST TWO COLUMNS OF THE DATAFRAME
_10kwords = _10kwords.iloc[:, 1:-4]
_6kwords = _6kwords.iloc[:, 1:-1]



Verb = _6kwords[_6kwords['Part'] == 'Verb']

Noun = _6kwords[
    (_6kwords['Part'] == 'Noun') |
    (_6kwords['Part'] == 'Interjection') |
    (_6kwords['Part'] == 'Verbal Noun') |
    (_6kwords['Part'] == 'Noun; Na-adjective; No-adjective') |
    (_6kwords['Part'] == 'Pronoun') |
    (_6kwords['Part'] == 'None') |
    (_6kwords['Part'] == 'nan') |
    (_6kwords['Part'].isna())  # Include rows where 'Part' is NaN
]

Adjective = _6kwords[
    (_6kwords['Part'].str.contains('Adv', na=False)) |
    (_6kwords['Part'].str.contains('Adj', na=False))
]




_01kwords_head = _10kwords.head(100)
_1kwords_head = _10kwords.head(1000)
_2kwords_head = _10kwords.head(2000)
_3kwords_head = _10kwords.head(3000)
_5kwords_head = _10kwords.head(5000)
_10kwords_head = _10kwords.head(10000)



# Assuming _6kwords and _10kwords are your DataFrames
noun_html = Noun.to_html()
verb_html = Verb.to_html()
adj_html = Adjective.to_html()
_01kwords_html = _10kwords.to_html()
_1kwords_html = _10kwords.to_html()
_2kwords_html = _10kwords.to_html()
_3kwords_html = _10kwords.to_html()
_5kwords_html = _10kwords.to_html()
_10kwords_html = _10kwords.to_html()


noun_soup = BeautifulSoup(noun_html, 'html.parser')
verb_soup = BeautifulSoup(verb_html, 'html.parser')
adj_soup = BeautifulSoup(adj_html, 'html.parser')
_01kwords_soup = BeautifulSoup(_01kwords_html, 'html.parser')
_1kwords_soup = BeautifulSoup(_1kwords_html, 'html.parser')
_2kwords_soup = BeautifulSoup(_2kwords_html, 'html.parser')
_3kwords_soup = BeautifulSoup(_3kwords_html, 'html.parser')
_5kwords_soup = BeautifulSoup(_5kwords_html, 'html.parser')
_10kwords_soup = BeautifulSoup(_10kwords_html, 'html.parser')

#export all the below tables in a html file; export all the previous tables in a html file

with open('raw/noun.html', 'w', encoding='utf-8') as f:
    f.write(noun_soup.prettify())
with open('raw/verb.html', 'w', encoding='utf-8') as f:
    f.write(verb_soup.prettify())
with open('raw/adj.html', 'w', encoding='utf-8') as f:
    f.write(adj_soup.prettify())
with open('raw/_01kwords.html', 'w', encoding='utf-8') as f:
    f.write(_01kwords_soup.prettify())
with open('raw/_1kwords.html', 'w', encoding='utf-8') as f:
    f.write(_1kwords_soup.prettify())
with open('raw/_2kwords.html', 'w', encoding='utf-8') as f:
    f.write(_2kwords_soup.prettify())
with open('raw/_5kwords.html', 'w', encoding='utf-8') as f:
    f.write(_5kwords_soup.prettify())
with open('raw/_10kwords.html', 'w', encoding='utf-8') as f:
    f.write(_10kwords_soup.prettify())



import os
from bs4 import BeautifulSoup, Comment

# Directory containing the HTML files
directory = r'C:\Users\pc\pyprojects\KanjiList\kanjilist-live\raw'

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








