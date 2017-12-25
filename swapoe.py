def swapoe(string):
	news=''
	new=''
	n=len(string)
	for i in range(n):
		if i%2 !=0 :
			new+=string[i]
		if i%2 == 0:
			news+=string[i]
	string=''
	for i in range(len(news)):
		if len(new)!=i:
			string+=new[i]
		string+=news[i]
	print(string)
	
def main():
	try:
		strin=input()
		swapoe(strin)
	except:
		print('invalid')
main()
		
