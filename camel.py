def camel(string):
	a=string.split(' ')
	s='' 
	for i in range(len(a)):
		a[i]=a[i].capitalize()
		s+=a[i]+' '
	print(s)
def main():
  try:
    string=input()
    camel(string)
  except:
    print('invalid')
main()
