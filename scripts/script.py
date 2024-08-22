import pandas as pd
import os

# Function to convert list of dictionaries into an HTML table
def convert_to_html_table(data):
    if not data:
        return "<table><tr><td>No data available</td></tr></table>"

    # Generate HTML for table headers
    headers = data[0].keys()
    table_headers = ''.join(f"<th>{header}</th>" for header in headers)
    
    # Generate HTML for table rows
    table_rows = ''.join(
        f"<tr>{''.join(f'<td>{row.get(header, '')}</td>' for header in headers)}</tr>"
        for row in data
    )
    
    # Combine headers and rows into a complete table
    html_table = f"<table border='1'><thead><tr>{table_headers}</tr></thead><tbody>{table_rows}</tbody></table>"
    return html_table

# Paths to the files
csv_file_path = "C:/Users/pc/pyprojects/KanjiList/kanjilist-live/backend_kanji.csv"
html_template_path = "C:/Users/pc/pyprojects/KanjiList/kanjilist-live/base.html"
output_directory = "C:/Users/pc/pyprojects/KanjiList/kanjilist-live/kanji"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Load the CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Read the HTML template
with open(html_template_path, 'r', encoding='utf-8') as file:
    html_template = file.read()

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Create a copy of the HTML template for this row
    html_content = html_template
    
    # Iterate over each column and replace placeholders with spaces
    for column in df.columns:
        # Handle the special case for table_data with |safe
        if column == "table_data":
            placeholder = f"{{{{ {column}|safe }}}}"  # This matches the special {{ table_data|safe }} placeholder
            if placeholder in html_content:
                # Convert the table_data value into an HTML table
                table_data = eval(row[column])  # Convert the string representation of list of dicts back to list of dicts
                value = convert_to_html_table(table_data)
                # Replace the placeholder with the converted value
                html_content = html_content.replace(placeholder, value)
        else:
            # Regular placeholder for other columns
            placeholder = f"{{{{ {column} }}}}"  # This matches the standard {{ variable }} placeholder
            if placeholder in html_content:
                value = str(row[column])
                # Replace the placeholder with the corresponding value
                html_content = html_content.replace(placeholder, value)
    
    # Save the modified HTML to a new file
    output_file_path = os.path.join(output_directory, f"{row[df.columns[0]]}.html")
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)
    
    print(f"Saved: {output_file_path}")
