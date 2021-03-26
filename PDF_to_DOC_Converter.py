import os
name = input('Enter the name with path of file : ')
os.rename(name,name[:-3]+'docx')
print("File converted successfully...")