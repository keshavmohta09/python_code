import marshal, pickle, json
d = {'b':'a','name':'Keshav','nullname':'KeshavMohta','cge':18}
s = pickle.dumps(d)
# a=marshal.loads(s)
print(s)
# json