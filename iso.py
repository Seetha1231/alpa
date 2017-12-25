def isomor(str1,str2):
	m=len(str1)
	n=len(str2)
	map=[-1]*256
	marked=[False]*256
	if m!=n:
		return False
	for i in range(n):
		if map[ord(str1[i])]==-1:
			if marked[ord(str2[i])]==True:
				return False
			marked[ord(str2[i])]=True
			map[ord(str1[i])]=str2[i]
		elif map[ord(str1[i])]!=str2[i]:
			return False
			
def main():
	s1=input()
	s2=input()
	isomor(s1,s2)
 
main()
