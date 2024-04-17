import xml.etree.ElementTree as ET

tree = ET.parse('./XML/1_ADR23Q4.xml')
root = tree.getroot()

elements_to_remove = [
    'primarysource', 'primarysourcecountry', 'occurcountry', 'transmissiondateformat',
    'transmissiondate', 'reporttype', 'receivedateformat', 'receivedate', 'receiptdateformat',
    'receiptdate', 'fulfillexpeditecriteria', 'companynumb', 'sender', 'receiver', 'duplicate', 'reportduplicate'
]

root.remove(root.find('ichicsrmessageheader'))

def should_process_safetyreport(safetyreport):
    patient = safetyreport.find('.//patient')
    if patient is None:
        return False  # Ignore if no patient
    if patient.find('.//patientsex') is None:
        return False  # Ignore if no patientsex
    if patient.find('.//patientonsetage') is None:
        return False  # Ignore if no patientonsetage
    drugs = patient.findall('.//drug')
    if any(drug.find('.//medicinalproduct') is None for drug in drugs):
        return False  # Ignore if any drug without medicinalproduct
    reactions = patient.findall('.//reaction')
    if any(reaction.find('.//reactionmeddrapt') is None for reaction in reactions):
        return False  # Ignore if any reaction without reactionmeddrapt
    return True

new_root = ET.Element(root.tag)

for safetyreport in list(root.findall('.//safetyreport')):
    if not should_process_safetyreport(safetyreport):
        root.remove(safetyreport)
        continue  # Skip processing this safetyreport
    
    for element_name in elements_to_remove:
        element = safetyreport.find(element_name)
        if element is not None:
            safetyreport.remove(element)

modified_xml_file_path = 'data_files/final_modified_XML.xml'

tree = ET.ElementTree(root)
tree.write(modified_xml_file_path, encoding='utf-8', xml_declaration=True)

print(f"The modified XML is saved to: {modified_xml_file_path}")
