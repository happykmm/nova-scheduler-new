import xml.etree.ElementTree as ET
import os

root_path = os.path.split(os.path.realpath(__file__))[0] + '/Data/input/initplace'


tree = ET.parse(root_path + '/test30/xml2.xml')


print tree

tree.write(root_path + '/test31/xml2.xml')
