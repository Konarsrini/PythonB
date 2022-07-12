"""
1. Create a python method that takes arguments int X and int Y,
and updates DEPART and RETURN fields
in test_payload1.xml:

- DEPART gets set to X days in the future from the current date
(whatever the current date is at the moment of executing the code)
- RETURN gets set to Y days in the future from the current date

Please write the modified XML to a new file.
Name and path of test_payload1.xml is to be mentioned.
New xml name: test_payload2.xml ; Path may have to be changed as needed
"""
#========================================================================
class AlterReservationXML:
    def __init__(self,intDepfromCurrDt,intRetfromCurrDt):
        if intRetfromCurrDt < intDepfromCurrDt:
            return
        import xml.etree.ElementTree as ET
        from datetime import timedelta
        from datetime import datetime
        mytree = ET.parse("Q:\\AA\\BB\\XMLJSONData\\test_payload1.xml")
        myroot = mytree.getroot()
        intDepDt = datetime.now()+timedelta(days=intDepfromCurrDt)
        intDepDt = intDepDt.strftime("%d%m%Y")
        intRetDt = datetime.now()+timedelta(days=intRetfromCurrDt)
        intRetDt = intRetDt.strftime("%d%m%Y")

        for name in myroot.iter('DEPART'):
            name.text = name.text.replace(name.text,intDepDt)
        for name in myroot.iter('RETURN'):
            name.text = name.text.replace(name.text,intRetDt)
        mytree.write("P:\\AAA\\BBB\\XMLJSONData\\test_payload2.xml")
#AlterReservationXML(10,15)
#========================================================================