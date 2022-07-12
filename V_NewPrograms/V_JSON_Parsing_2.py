#import json
strFile = "G:\\PythonTrials\\MyPythonPrograms\\XMLJSONData\\test_payload.json"
strFile2 = "G:\\PythonTrials\\MyPythonPrograms\\XMLJSONData\\test_payload2.json"
#Obj = json.load(open(strFile))
#print(Obj)

import json

jsonpath = strFile

with open(jsonpath) as file:
    j = json.loads(file.read())
names_to_remove = ['outParams']
print(j)
#================================
strL = []
for eachelement in j:
    strL.append(eachelement)
#================================
strLE = 'appdate'
for EachLE in strL:
    for element in j[EachLE][strLE]:
        del j[EachLE][strLE]
        break
#=====================================
"""Wrk

for element in j['inParams']['appdate']:
    del j['inParams']['appdate']
    break
"""
"""wrks
for element in j['inParams']:
    print(element)
    print(type(element))
    if element == 'appdate':
        print(type(j['inParams']['appdate']))
        del j['inParams']['appdate']
        break
for element in j:
    if element == 'outParams':
        print(type(j['outParams']))
        #del j['outParams']
        break
"""
"""        
open("G:\PythonTrials\MyPythonPrograms\XMLJSONData\\test_payload2.json", "w").write(
    json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))
"""
"""
    if element['inParams'] in names_to_remove:
        j['inParams'].remove(element)s
with open(strFile2, 'w') as file:
    file.write(json.dumps(j, indent=4))

with open(strFile, "w") as write_file:
    json.dump(Obj, write_file)
for element in Obj:
    if element.get("appdate") is not None:
        if element["appdate"].get("2019-04-02") is not None:
            print("d")
                #del element["fields"]["idb_metric"]
open("G:\PythonTrials\MyPythonPrograms\XMLJSONData\test_payload2.json", "w").write(
    json.dumps(Obj, sort_keys=True, indent=4, separators=(',', ': '))
)



for element in data:
        del element["fields"]["idb_metric"]

    print(element["fields"])

class AlterReservationXML:
    def __init__(self,intDepfromCurrDt,intRetfromCurrDt):
        if intRetfromCurrDt < intDepfromCurrDt:
            return
        import xml.etree.ElementTree as ET
        from datetime import timedelta
        from datetime import datetime
        mytree = ET.parse("G:\\PythonTrials\\MyPythonPrograms\\XMLJSONData\\test_payload1.xml")
        myroot = mytree.getroot()
        intDepDt = datetime.now()+timedelta(days=intDepfromCurrDt)
        intDepDt = intDepDt.strftime("%d%m%Y")
        intRetDt = datetime.now()+timedelta(days=intRetfromCurrDt)
        intRetDt = intRetDt.strftime("%d%m%Y")

        for name in myroot.iter('DEPART'):
            name.text = name.text.replace(name.text,intDepDt)
        for name in myroot.iter('RETURN'):
            name.text = name.text.replace(name.text,intRetDt)
        mytree.write("G:\\PythonTrials\\MyPythonPrograms\\XMLJSONData\\test_payload2.xml")
#AlterReservationXML(10,15)

if name.attrib['DEPART']:
    print(name.attrib['DEPART'])
    name.attrib['DEPART'] = name.attrib['DEPART'].replace('20191225', '20191225112')
"""
#tree.write('example.xml')
"""
for x in myroot.iter('DEPART'):
    #print(x.tag,x.items(),x.attrib,x.text)
    x.set('DEPART',intDepDt)
    #print(x.tag, x.items(), x.attrib, x.text)
#for x in myroot.iter('DEPART'):
    #print(x.tag,x.items(),x.attrib,x.text)
mytree.write("G:\\PythonTrials\\MyPythonPrograms\\XMLJSONData\\test_payload2.xml")

from xml.dom import minidom
from xml.dom.minidom import Document
# noinspection PyUnresolvedReferences
from xml.dom.minidom import Element
import xml.dom.minidom
strXML1 = r'G:\PythonTrials\MyPythonPrograms\XMLJSONData\test_payload1.xml'
strXML2 = "G:\\PythonTrials\\MyPythonPrograms\\XMLJSONData\\test_payload2.xml"

xmldoc = minidom.parse(strXML1)
tags = xmldoc.getElementsByTagName('TP')
print(tags)
for item in tags:
    print(item)
    str = item.attributes['DEPART'].value
    #strA = item.attributes['DEPART'].value
    print(str)
"""