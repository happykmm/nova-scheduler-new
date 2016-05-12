import xml.etree.ElementTree as ET
import os
import commands

root_path = os.path.split(os.path.realpath(__file__))[0]
input_path = root_path + '/Data/input/initplace'

tree = ET.parse(input_path + '/test30/xml2.xml')

print tree
# fill the xml file here

tree.write(input_path + '/test31/xml2.xml')

drs_retcode, drs_output = commands.getstatusoutput("echo '1 31 0' | " + root_path + "/drs03")
print drs_retcode
print drs_output
