def max(l):
	max=0
	for i in l:
		if max<i:
			max=i
	print(max)
def main():
	try:
		l=[1,2,3,5,4,77,4,24,52,4]
		max(l)
	except:
		print('invalid')
main()
