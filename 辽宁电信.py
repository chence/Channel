import re
from DPL频道列表模板 import list
import string
import re
import os
file=open("C:\\Users\\Administrator\\Desktop\\node\\辽宁电信.txt","r+",encoding='utf-8')
f=file.read()
p1=r'.+?,'
pattern1=re.compile(p1)
name=pattern1.findall(f)
names=[]
for x in range(len(name)):
    y=name[x].replace(",","")
    names.append(y)
#print(names)
p2=r'http.+?_CMSID=&Fsv_otype=1'
pattern2=re.compile(p2)
url=pattern2.findall(f)
print(len(url))
print(len(names))
with open('辽宁电信.dpl', 'a', encoding="utf-8") as f: f.write('DAUMPLAYLIST\n'+'playname=\n'+'topindex=27\n'+'saveplaypos=0')
for u in url:
    j=url.index(u)
    (x,y)=list(names[j],u)
    with open('辽宁电信.dpl', 'a+', encoding="utf-8") as f: f.write(str(j+1)+x + "\n"+str(j+1)+y+"\n"+str(j+1)+'*played*0\n')
file.close()
os.system('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Daum\\PotPlayer 64 bit.exe')
os.system('C:\\Users\\Administrator\\PycharmProjects\\频道破解\\辽宁电信.dpl')
'''keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print dictionary
'''