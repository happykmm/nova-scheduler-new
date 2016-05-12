import xml.etree.ElementTree as ET
import os

root_path = os.path.split(os.path.realpath(__file__))[0]
file_path = root_path + '/Data/input/initplace/test30/xml2.xml'

tree = ET.parse(file_path)

print tree
