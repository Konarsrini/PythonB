REM ======================================================
REM wscript "G:\VBS\VB_LibraryFunctions\WerService_anyREQUEST.vbs" "POST" """https://demoqa.com/BookStore/v1/Books"" -H ""accept: REM application/json"" -H ""Content-Type: application/json"" -d ""{ ""userId"": ""ToolsToolsTools"", ""collectionOfIsbns"": [ { ""isbn"": ""9781456725862"" } ]}""" "" ""
REM ======================================================
REM wscript "G:\VBS\VB_LibraryFunctions\WerService_anyREQUEST.vbs" "GET" "https://demoqa.com/BookStore/v1/Books"" -H ""accept: application/json" "" ""
REM ======================================================
REM wscript "G:\VBS\VB_LibraryFunctions\WerService_anyREQUEST.vbs" "GET" "https://demoqa.com/BookStore/v1/Books" "" "" ""
REM ======================================================
REM wscript "G:\VBS\VB_LibraryFunctions\WerService_anyREQUEST.vbs" "POST" "https://demoqa.com/BookStore/v1/Books" "" ""
REM wscript "G:\VBS\VB_LibraryFunctions\WerService_anyREQUEST.vbs" "POST" "http://restapi.adequateshop.com/api/Tourist" "" "" "{8$9tourist_name8$9: 8$9Pike8$9,8$9tourist_email8$9: 8$9pike2_new1_123@gmail.com8$9,8$9tourist_location8$9: 8$9Paris8$9}"
REM ======================================================
REM wscript "G:\VBS\VB_LibraryFunctions\WerService_anyREQUEST.vbs" "PUT" "http://restapi.adequateshop.com/api/Tourist" "" "" "{8$9tourist_name8$9: 8$9Pike8$9,8$9tourist_email8$9: 8$9pike2_new1_123@gmail.com8$9,8$9tourist_location8$9: 8$9Bonn8$9}"
wscript "G:\VBS\VB_LibraryFunctions\WerService_anyREQUEST.vbs" "DELETE" "http://restapi.adequateshop.com/api/Tourist" "" "" "{8$9tourist_name8$9: 8$9Pike8$9,8$9tourist_email8$9: 8$9pike2_new1_123@gmail.com8$9,8$9tourist_location8$9: 8$9Paris8$9}"