import re
f=open('indonesia.txt','r', encoding='latin1')
teks = f.read()
f.close()
print(re.findall(r'me\w+',teks.lower()))
print("\n")

