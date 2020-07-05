#Nomor 4a
print("No 4a---------------------------------------------------------------------------------------------------------------------------------------------------------")
import re
f=open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
print(re.findall(r'([\w+]+)</a></td>',teks4))
print("\n")

#Nomor 4b
print("No 4b---------------------------------------------------------------------------------------------------------------------------------------------------------")
f=open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
string=re.findall(r'title="([\w+]+)">',teks4)
string=re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks4)
a=[]
for i in string:
    a.append((i[0], float(i[1])))
print(a)
