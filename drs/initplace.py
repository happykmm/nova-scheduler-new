import xml.etree.ElementTree as ET
import os
import commands


class Initplace:

    def __init__(self):
        self.root_path = os.path.split(os.path.realpath(__file__))[0]
        self.input_path = self.root_path + '/Data/input/initplace'
        self.__xml2 = ET.parse(self.input_path + '/sample/xml2.xml')

    def get_xml2(self):
        return self.__xml2

    def set_xml2(self):
        self.__xml2.write(self.input_path + '/test30/xml2.xml')

    def do_schedule(self):
        cmd = "cd " + self.root_path + "; echo '1 30 0' | " + self.root_path + "/drs03"
        retcode, output = commands.getstatusoutput(cmd)
        print retcode
        xml3 = ET.parse(self.input_path + '/test30/xml3.xml')
        print xml3

