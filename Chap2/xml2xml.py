import os;

__author__='Shafin Thiyam'
class xml_processsing:
    def __init__(self,xsl,input_xml):
        self.xsl=xsl
        self.input_xml=input_xml

    def tranformation(self):
        print("processing started...")
        if self.input_xml.endswith('txt'):
            input_list = open(self.input_xml).read().split("\n")
            for i in input_list:
                os.system("java net.sf.saxon.Transform -s:{0} -xsl:{1} -o:{2}_output.xml".format(i,self.xsl,i.split('.')[0]))
            #os.system("java net.sf.saxon.Transform -s:{0} -xsl:{1} -o:{2}_output.xml".format(i,self.xsl,i.split('.')[0]) for i in input_list)
        else:
            os.system("java net.sf.saxon.Transform -s:{0} -xsl:{1} -o:{2}_output.xml".format(self.input_xml,self.xsl,self.input_xml.split('.')[0]))

        print("processing Completed")