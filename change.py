import os
import re

# Define the new <head> content
new_head_content = '''<head>
    <title>KanjiList.org</title>
    
    <!-- Meta Tags -->
    <meta charset="UTF-8">
    <meta name="author" content="Alejandro Moral">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="kanji, study, kanji cards, kanji flashcards, kanji order, stroke order, japanese kanji">
    <meta name="description" content="Sorted lists of Kanji according to your preferences along with information for writing your own Kanji cards.">
    
    <!-- Stylesheet -->
    <link rel="stylesheet" type="text/css" href="/static/css/style.css" title="default style">
    
    <!-- Favicon -->
    <link rel="icon" href="/static/icons/favicon.png" type="image/png">
    
    <!-- Schema Markup -->
    <script type="application/ld+json">
    {
        "@context": "http://schema.org",
        "@type": "Organization",
        "name": "Kanjilist",
        "url": "http://www.kanjilist.org",
        "logo": "http://www.kanjilist.org/static/icons/favicon.png"
    }
    </script>
    
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){
        w[l]=w[l]||[];
        w[l].push({'gtm.start': new Date().getTime(), event: 'gtm.js'});
        var f = d.getElementsByTagName(s)[0],
            j = d.createElement(s),
            dl = l != 'dataLayer' ? '&l=' + l : '';
        j.async = true;
        j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
        f.parentNode.insertBefore(j, f);
    })(window, document, 'script', 'dataLayer', 'GTM-TG7ZKBSS');</script>
    <!-- End Google Tag Manager -->
</head>
'''

# Directory containing HTML files
directory = r'C:\Users\pc\pyprojects\KanjiList\kanjilist-live'

# Function to update <head> section in a file
def update_head(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regular expression to find and replace the <head> section
    new_content = re.sub(r'<head>.*?</head>', new_head_content, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Loop through all HTML files in the directory and update them
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        file_path = os.path.join(directory, filename)
        update_head(file_path)

print("All HTML files have been updated.")
