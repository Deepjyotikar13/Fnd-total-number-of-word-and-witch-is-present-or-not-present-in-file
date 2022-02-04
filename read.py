#you can modify this project and also count number and this project will tell you witch is not present
#you have to give the diractary in open() function and user you can give the file name or you can give a file name
alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

user=input("Enter file name::")
with open(f'/storage/emulated/0/{user}.txt') as d:
	k=d.read()
	#print(k.upper())
	lis=k.upper()
	lis2=list(lis)
	lis5=[]
	lisforcount=[]
	for i in alpha:
		if i in lis2:
			h=i
			print("alphabate:",h,":is present =",lis2.count(h))
			klj=lis2.count(h)
			lisforcount.append(klj)
			lis5.append(h)
	
		else:
			pass
			
	#print(lis5)
	#lis5
	hjlis=[]
	for j in alpha:
		if j  in lis5:
			pass
		else:
			hjlis.append(j)
	print(hjlis,"is not present")
	print("total word is::",sum(lisforcount))

