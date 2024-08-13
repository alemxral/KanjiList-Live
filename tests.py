import ast

def convert_to_html_table(python_literal_string):
    # Parse the Python literal string into a list of dictionaries
    try:
        data = ast.literal_eval(python_literal_string)
    except (ValueError, SyntaxError) as e:
        print(f"Error decoding string: {e}")
        return ""

    # Start building the HTML table
    html_table = "<table border='1'>\n"
    html_table += "  <thead>\n    <tr>\n"
    
    # Add table headers based on keys in the first dictionary
    if data:
        for key in data[0].keys():
            html_table += f"      <th>{key}</th>\n"
        html_table += "    </tr>\n  </thead>\n"

    # Add table rows
    html_table += "  <tbody>\n"
    for entry in data:
        html_table += "    <tr>\n"
        for value in entry.values():
            html_table += f"      <td>{value}</td>\n"
        html_table += "    </tr>\n"
    html_table += "  </tbody>\n</table>"

    return html_table

if __name__ == "__main__":
    # Example string input with properly escaped quotes
    python_literal_string = '''[
        {'Word': '梓', 'Reading': 'あずさ, し, アズサ', 'Meaning': 'Japanese cherry birch (Betula grossa); yellow catalpa (Catalpa ovata); printing block'},
        {'Word': '梓弓', 'Reading': 'あずさゆみ', 'Meaning': 'catalpa bow, betula grossa'},
        {'Word': '上梓', 'Reading': 'じょうし', 'Meaning': 'publication, wood-block printing'},
        {'Word': '梓宮', 'Reading': 'しきゅう', 'Meaning': "Emperor's coffin (made of catalpa wood)"},
        {'Word': '梓匠', 'Reading': 'ししょう', 'Meaning': 'cabinetmaker, woodworker'},
        {'Word': '梓に上せる', 'Reading': 'しにのぼせる', 'Meaning': 'to bring (a book) into the world, to publish'}
    ]'''

    # Convert to HTML table
    html_table = convert_to_html_table(python_literal_string)

    # Print the resulting HTML table
    print(html_table)
