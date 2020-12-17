from json import dumps
dictionary = dict()
while True:
    i = input("For add item press any key else press Enter : ")
    if i=='':
        break
    keyvalue = input('Enter key-value : ').split('-')
    dictionary[keyvalue[0]] = keyvalue[1]
jsondict = dumps(dictionary,indent=4)
print(jsondict)