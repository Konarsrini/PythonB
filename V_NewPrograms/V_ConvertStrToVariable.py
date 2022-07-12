#=============This will convert a string name to a variable name)=============#
str = 'pythonpool'
print(str)
locals()[str] = 'New string'
print('pythonpool')
print(pythonpool)
print(str)