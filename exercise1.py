try:
	file1=open('brown.txt')
except:
	print('File cannot be opened:', file1)
	exit()
lines=file1.readlines()
file1.close()
dict={}
file2=open('output.txt','w')

for line in lines:
	words=line.split()
	length=len(words)

	for i in range(length-1):
		key=words[i]+' '+words[i+1]
		if key not in dict:
			dict[key]=1
		else:
			dict[key]+=1

sum=0
for key in dict:
	res=key,dict[key]
	file2.write(str(res))
	file2.write('\n')
#average eseptey
	sum+=dict[key]
ave=sum/len(dict)

print('Average:',ave, '\nSumma:',sum, '\nDlina dict:',len(dict))


