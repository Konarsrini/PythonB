"""
V_FunctionFunction.py has following content:
def my_function7A(test):
  print("The called function is my_function7A. Parameter is "+str(test))

def my_function8A(test):
  print("The called function is my_function8A. Parameter is "+str(test))  
""" #TBD pythonpath
"""
#===================================================
#Method 1:
from FunctionRepository import V_FunctionFunction
V_FunctionFunction.my_function7A("Hi there")
V_FunctionFunction.my_function8A("Hello there")
#The called function is my_function7A. Parameter is Hi there
#The called function is my_function8A. Parameter is Hello there
"""
#===================================================
#Method 2:
#Call function placed anywhere . Append sys.path with the new folder name
import sys
sys.path.append('G:/PythonTrials/MyPythonPrograms/FunctionRepository')

import V_FunctionFunction
V_FunctionFunction.my_function7A("Hi there")
V_FunctionFunction.my_function8A("Hi Here and there")
#===================================================

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")