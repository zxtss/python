#coding=utf-8
import re
x = input('Please input a string:')
pattern = re.compile(r'\b[a-zA-Z]{3}\b')
print(pattern.findall(x))



'''import re
x='This is a a desk'
pattern=re.compile(r'\b(\w+)(\s+\1){1,}\b')
matchResult=pattern.search(x)
x=pattern.sub(matchResult.group(1),x)
print(x)
'''



'''import re
x = "I am a teacher,I am man, and I am 38 years old.I am not a busInessman."
print(x)
pattern = re.compile(r'(?:[\w])I(?:[\w])')
while True:
    result = pattern.search(x)
    if result:
        if result.start(0)!= 0:
            x = x[:result.start(0)+1]+'i'+x[result.end(0)-1:]
        else:
            x = x[:result.start(0)]+'i'+x[result.end(0)-1:]
    else:
        break
print(x)
'''


'''x = "i am a teacher,i am man, and i am 38 years old.I am not a businessman."
import re
pattern = re.compile(r'(?:[^\w]|\b)i(?:[^\w])')
while True:
	result=pattern.search(x)
	if result:
		if result.start(0)!=0:
			x=x[:result.start(0)+1]+'T'+x[result.end(0)-1:]
		else:
			x=x[:result.start(0)]+'T'+x[result.end(0)-1:]
	else:
		break
print(x)
'''
