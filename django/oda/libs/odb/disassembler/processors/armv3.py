'''
Created on November 7, 2012

@author: Owner
'''
from oda.libs.odb.disassembler.processors.arm import arm

class armv3(arm):
    def __init__(self, odb_file):
        arm.__init__(self, odb_file)