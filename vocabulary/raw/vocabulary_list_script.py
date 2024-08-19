import pandas as pd
import os
from bs4 import BeautifulSoup


#import xlsx file
_10kwords = pd.read_excel('vocabulary/raw/10Kwords.xlsx') 
_6kwords = pd.read_excel('vocabulary/raw/6Kwords.xlsx') 

#eliminate THE LAST TWO COLUMNS OF THE DATAFRAME
_10kwords = _10kwords.iloc[:, 1:-3]
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


# print(len(Verb))
# print(len(Noun))
# print(len(Adjective))

# sum = len(Verb) + len(Noun) + len(Adjective)
# print(sum)
# # #save in a matrix all the unique values of the column called Part
# # unique = _6kwords['Part'].unique()
# # print(unique)

_01kwords_head = _10kwords.head(100)
_1kwords_head = _10kwords.head(1000)
_2kwords_head = _10kwords.head(2000)
_3kwords_head = _10kwords.head(3000)
_5kwords_head = _10kwords.head(5000)
_10kwords_head = _10kwords.head(10000)



# Assuming _6kwords and _10kwords are your DataFrames
noun_html = _6kwords.to_html()
verb_html = _6kwords.to_html()
adj_html = _6kwords.to_html()
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

with open('vocabulary/raw/noun.html', 'w', encoding='utf-8') as f:
    f.write(noun_soup.prettify())
with open('vocabulary/raw/verb.html', 'w', encoding='utf-8') as f:
    f.write(verb_soup.prettify())
with open('vocabulary/raw/adj.html', 'w', encoding='utf-8') as f:
    f.write(adj_soup.prettify())
with open('vocabulary/raw/_01kwords.html', 'w', encoding='utf-8') as f:
    f.write(_01kwords_soup.prettify())
with open('vocabulary/raw/_1kwords.html', 'w', encoding='utf-8') as f:
    f.write(_1kwords_soup.prettify())
with open('vocabulary/raw/_2kwords.html', 'w', encoding='utf-8') as f:
    f.write(_2kwords_soup.prettify())
with open('vocabulary/raw/_5kwords.html', 'w', encoding='utf-8') as f:
    f.write(_5kwords_soup.prettify())
with open('vocabulary/raw/_10kwords.html', 'w', encoding='utf-8') as f:
    f.write(_10kwords_soup.prettify())







