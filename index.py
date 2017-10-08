#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
imports os
directory = sys.argv[1]
filename = sys.argv[2]
paths = os.walk(directory)
for root,dirs,files in paths:    
    if filename in files:
        print 'Yes'
        breaks
else:
    print 'No'

'''#文件移动
import shutil
shutil.move(r'd:\1.txt',r'h:\\1.txt')
'''

'''import pickle
d = {'张三':98,'李四':90,'王五':100}
print(d)
f = open('score.dat','wb')
pickle.dump(1,f)
pickle.dump(d,f)
f.close

f = open('score.dat','rb')
pickle.load(f)
d = pickle.load(f)
f.close()
print(d)
'''
'''
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''

'''
 f = open(r'd:\zxt.txt','r')
s = f.readlines()
f.close()
r = [i.swapcase() for i in s]

f = open(r'd:\2.txt','w')
f.writelines(r)
f.close()
print s
'''

'''x = "i am a teacher,i am man, and i am 38 years old.I am not a businessman."
x=x.replace('i','I')
print (x)
'''

#字典的特性，不允许同一个键出现两次，如果出现两次后一个键就会被记住

'''x=input('Please input  x:')
if x<0 or x>=20:
	print (0)
elif 0<=x<5:
	print (x)
elif 5<=x<10:
	print (3*x-5)
elif 10<=x<20:
	print  (0.5*x-2)

'''

'''
x=[i for i in range(1,100) if i%2==1]
print (sum(x))
print (sum (range(1,100)[::2]))





x = input('Please input an integer less than 1000:')
t = x
i = 2
result = []
while True:
    if t==1:
        break
    if t%i==0:
        result.append(i)
        t = t/i
    else:
        i+=1
print(x,'=','*'.join(map(str,result)))




import random 
x=[random.randint(0,100) for i in range(20)]
print(x)
y=x[::2]
y.sort(reverse=True)
x[::2]=y
print (x)




import random
x=[random.randint(0,100) for i in range(50)]
print(x)
i=len(x)-1
while i>=0:
	if x[i]%2==1:
		del x[i]
	i-=1
print(x)



x = input('Please input an integer of 4 digits meaning the year:')

if x%400==0 or (x%4==0 and not x%100==0):
    print('Yes')
else:
    print('No')
 '''