import subprocess
import os;
import sys;

class xml_processsing:
    def __init__(self,input_xml,xsl,output):
        self.input_xml=input_xml
        self.xsl=xsl
        self.output=output

    def tranformation(self):
        os.system("java net.sf.saxon.Transform -s:{0} -xsl:{1} -o:{2}".format(self.input_xml,self.xsl,self.output))



