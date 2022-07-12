"""
2. Create a python method that takes a json element
as an argument, and removes that element from test_payload.json.

Please verify that the method can remove either nested or non-nested elements
(try removing "outParams" and "appdate").
strFile : name and path of test_payload.json needs to be provided
strFile2 : name and path of new json to be provided
"""
class Cls_RemoveElementfromJSon:
    def __init__(self,strElm):
        strFile = "G:\\PythonTrials\\MyPythonPrograms\\XMLJSONData\\test_payload.json"
        strFile2 = "G:\\PythonTrials\\MyPythonPrograms\\XMLJSONData\\test_payload2.json"
        import json
        import time
        jsonpath = strFile

        with open(jsonpath) as file:
            j = json.loads(file.read())
        #================================
        strL = []
        for eachelement in j:
            strL.append(eachelement)
        print(strL)
        #================================
        while True:
            strD = ""
            for eachelement in j:
                if eachelement == strElm:
                    print(eachelement)
                    del j[strElm]
                    print("strElm 1")
                    strD = "Y"
                    break
            if strD == "Y":
                break
            #================================
            for EachLE in strL:
                for element in j[EachLE]:
                    if element == strElm:
                        del j[EachLE][strElm]
                        print("strElm 2")
                        strD = "Y"
                        break
                if strD == "Y":
                    break
            if strD == "Y":
                break
        #=====================================
        open(strFile2, "w+").write(json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))
        time.sleep(2)
        #==========================================
        jsonpath = strFile2
        strPresent = "N"
        with open(jsonpath) as file:
            j = json.loads(file.read())
        # ================================
        strL = []
        for eachelement in j:
            strL.append(eachelement)
        # ================================
        for eachelement in j:
            if eachelement == strElm:
                strPresent = "Y"
        # ================================
        print(strL)
        for EachLE in strL:
            if strElm in strL:
                for element in j[EachLE]:
                    if element == strElm:
                        strPresent = "Y"
        # =====================================
        if strPresent == "Y":
            print(f'Fail: The Element {strElm} is present in new XML {strFile2}')
        else:
            print(f'Pass: The Element {strElm} isn\'t present in new XML {strFile2}')
#===============================
Cls_RemoveElementfromJSon("outParams")
#Cls_RemoveElementfromJSon("appdate")
#===============================