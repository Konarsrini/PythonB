"""
3. Create a python script that parses jmeter log files in CSV format,
and in the case if there are any non-successful endpoint responses recorded in the log,
prints out the label, response code, response message, failure message,
and the time of non-200 response in human-readable format in PST timezone
(e.g. 2021-02-09 06:02:55 PST).

Please use Jmeter_log1.jtl, Jmeter_log2.jtl as input files for testing out your script
(the files have .jtl extension but the format is  CSV).

strCSVFile1 is to be parsed

"""
#=================================================================================================
class ExtractGetMethodFailureinLog:
    def __init__(self,strCSVFile1):
        import csv
        #strCSVFile1 = "G:\\PythonTrials\\MyPythonPrograms\\PyQuestionsOrAssignments\\Updated_Python_exercises_QA_Engr\\Jmeter_log1.jtl"
        strRead = None
        with open(strCSVFile1) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                strRow1 = row
                if strRead == None:
                    inttimeStamp = strRow1.index("timeStamp")
                    intRlabel = strRow1.index("label")
                    intresponseCode = strRow1.index("responseCode")
                    intresponseMessage = strRow1.index("responseMessage")
                    intfailureMessage = strRow1.index("failureMessage")
                    intsuccess = strRow1.index("success")
                    strinttimeStamp = row[inttimeStamp]
                    strRlabel = row[intRlabel]
                    strresponseCode = row[intresponseCode]
                    strresponseMessage = row[intresponseMessage]
                    strfailureMessage = row[intfailureMessage]
                    strtimeStamp = row[inttimeStamp]
                    strRead = "Y"
                if row[intresponseCode] != '200':
                    print(f'Fail: strRlabel = {row[intRlabel]};strresponseCode = {row[intresponseCode]};strresponseMessage = {row[intresponseMessage]};strfailureMessage = {row[intfailureMessage]};strtimeStamp = {row[inttimeStamp]}')
#=================================================================================================
strCSVFile1 = "G:\\PythonTrials\\MyPythonPrograms\\PyQuestionsOrAssignments\\Updated_Python_exercises_QA_Engr\\Jmeter_log1.jtl"
ExtractGetMethodFailureinLog(strCSVFile1)