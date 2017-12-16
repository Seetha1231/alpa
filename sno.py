n=15
print('sum from 1-15 :'+str(n*(n+1)//2))
s=15
e=45
sum=0
for i in range(s,e+1):
	if i%2==0:
		continue
	sum+=i
print('sum of odd number from 15-45(included) :'+str(sum))
