# Neo4jToOWL
Neo4j Database To OWL File Conversion Using Python

## Project Files

- **modify_XML.py**  
  A Python script is used to modify and preprocess XML files. This prepares data by adjusting XML structures before they are converted to JSON, ensuring compatibility with subsequent loading processes.

- **xml_to_json.py**  
  This Python script converts XML data into a JSON format that is more suitable for ingestion by the Neo4j database. It is a critical part of the data preparation pipeline, facilitating the transition from raw FDA data formats to structured graph data.

- **cypher2.txt**  
  Contains Cypher queries for loading JSON data into the Neo4j database. It creates nodes and establishes relationships based on the structure of the FDA's adverse event reports. This script is essential for setting up the graph database schema and relationships like 
  'HAS_PATIENT' and 'EXPERIENCED'.

- **FDA_Ontology_Creation-checkpoint.ipynb**  
  A Jupyter notebook that provides detailed documentation of the ontology creation process. It includes Python code snippets for data manipulation that outline the methodology used during the ontology development.

- **ontology_with_subclasses2.owl**
  It is the final output OWL file generated.

## Setup Instructions

To properly use this repository's resources, please ensure you have Python and Neo4j installed on your system.

- **Downloading FDA Data**
    Quarterly data can be downloaded from the FAERS database. The URL is "https://fis.fda.gov/extensions/FPD-QDE-FAERS/FPD-QDE-FAERS.html".

- **Run Python Scripts**
    Execute the Python scripts on the downloaded data. First, modify the data and convert it into JSON, using the respective Python scripts.

- **Data Loading**
    Import the data into your Neo4j database using the Cypher queries in cypher2.txt.

- **OWL File Conversion**
    After loading the data into Neo4j, connect the database using the driver mentioned in the .ipynb file. Make sure your Neo4j server is running before connecting to the server. Execute the scripts in the .ipynb file and mention the destination where you want to download     the final .owl file.
   
