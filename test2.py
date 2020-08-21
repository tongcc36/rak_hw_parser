#!/usr/bin/env python
#-*- conding:utf-8 -*-
# with open(r"C:\test\config.txt",encoding='utf-8') as f:
txt = "EDKII Menu->Socket configuration->Processor configuration->Lock Chipset=Disable"
x = txt.split("->", -1)
print(x[-1])
x1=x[-1].split("=", -1)
print(x1[0])

from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("PlatformConfig.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print ("Root element : %s" % collection.getAttribute("shelf"))