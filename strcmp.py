def compare(str1,str2):
	if str1==str2:
		print(str2)
	elif str1>str2:
		print(str1)
	else :
		print(str2)
def main():
	try:
		s1=input()
		s2=input()
		compare(s1,s2)
	except:
		print('invalid')
main()
