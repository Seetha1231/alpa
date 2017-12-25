def uniq(string):
	r=[]
	for i in range(len(string)):
		if string[i] in r:
			continue
		r.append(string[i])
	print(''.join(r))
def main():
	str=input()
	uniq(str)
main()
 
   
