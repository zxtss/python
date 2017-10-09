'''
#-*- coding: utf-8 -*-
import random
x=[random.randint(0,100) for i in range(20)]
print(x)
y=x[0:10]
y.sort()
x[0:10]=y
y = x[10:20]
y.sort(reverse=True)
x[10:20] = y

print (x)
'''

'''d = {1:'a', 2:'b', 3:'c', 4:'d'}
v = input('Please input a key:')
print(d.get(v,'您输入的的键不存在'))
'''



'''
#-*- coding: utf-8 -*-
x = input('Please input a list:')
start, end = input('Please input the start position and the end position:')
print x[start:end]
'''



'''#-*- coding: utf-8 -*-
#编写生成包含1000个0到100之间的随机数，并统计每个元素的出现次数
import random
x = [random.randint(0,100) for i in range(1000)]
d = set(x)   #有序输出
for v in d:#迭代遍历器
    print(v, ':', x.count(v))

print random.randint(1,10)
random.seed(10)
print random.seed()

'''

'''
 #-*- coding: utf-8 -*-
 #第二种方式
import types
x = input('Please input an integer of more than 3 digits:')
if type(x) != types.IntType:
    print 'You must input an integer.'
elif len(str(x)) != 4:
    print 'You must input an integer of more than 3 digits.'
else:   
    print x//100
 '''
'''第一种方式
用户输入一个三位以上的整数，输出其百位以上的数字。
x=input('Please input an integer of more than 3 disgits:')
try:
    x=int(x)
    x=x//100
    if x==0:
        print('You must input an integer of more than 3 disgits')
    else:
        print(x)
except BaseException:
    print('You must input an integer.')
''' 