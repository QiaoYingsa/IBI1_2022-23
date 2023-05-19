import xml.etree.ElementTree as ET
from openpyxl import Workbook

# Parse the XML document
tree = ET.parse('go_obo.xml')
root = tree.getroot()

# Create an Excel workbook and sheet
workbook = Workbook()
sheet = workbook.active

# Write header row
sheet.append(['GO ID', 'Term Name', 'Definition String', 'Number of Child Nodes'])

# Iterate over the XML tree
for term in root.findall('.//term'):
    go_id = term.find('id').text
    name = term.find('name').text
    definition = term.find('def/defstr').text

    # Count the number of child nodes
    child_count = len(term.findall('.//is_a'))

    # Write data to the Excel sheet
    sheet.append([go_id, name, definition, child_count])

# Save the workbook
workbook.save('autophagosome.xlsx')
