import xml.etree.ElementTree as ET
import json

def xml_to_dict(element):
    
    # Base case:
    if not element:
        return element.text or ""
    
    # Recursive case: 
    result = {}
    for child in element:
        child_result = xml_to_dict(child)
        
        # Handle multiple children with the same tag
        if child.tag not in result:
            result[child.tag] = child_result
        elif isinstance(result[child.tag], list):
            result[child.tag].append(child_result)
        else:
            result[child.tag] = [result[child.tag], child_result]
    
    return result


tree = ET.parse('./data_files/final_modified_XML.xml')
root = tree.getroot()

xml_dict = xml_to_dict(root)

json_str = json.dumps(xml_dict, indent=4)

json_file_path = 'data_files/final_converted_JSON.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_str)

print(f"The XML has been converted to JSON and saved to: {json_file_path}")
