import xml.etree.ElementTree as ET
import os

file_path = os.path.split(os.path.realpath(__file__))[0]
print file_path

tree = ET.parse('Data/input/initplace/test30/xml2.xml')

print tree
