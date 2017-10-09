def Sorted(v):
	t=v[::]
	r=[]
	while t:
		tt=min(t)
		r.append(tt)
		t.remove(tt)
		return
	x=[1,3,5,7,9,2,0,4,1,2]
	print(x)
	print(Sorted(x))




'''def demo(v):
	capital=little=digit=other=0
	for i in v:
		if 'A'<=i<='Z':
			capital+=1
		elif 'a'<=i<='z':
			little+=1
		elif '0'<=i<='9':
			digit+=1
		else:
			other+=1
	return(capital,little,digit,other)
v = 'capital = little = digit = other =0'
print(demo(v))
'''



'''import math
def IsPrime(v):
    n = int(math.sqrt(v)+1)
    for i in range(2,n):
        if v%i==0:
            return 'No'
    else:
        return 'Yes'
print(IsPrime(37))
print(IsPrime(60))
print(IsPrime(113))
'''