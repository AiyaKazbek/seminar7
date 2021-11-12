try:
	file1=open('brown.txt')
except:
	print('File cannot be opened:', file1)
	exit()
lines=file1.readlines()
file1.close()
dict={}
count=0
sum=0
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

for key in dict:
	file2.write(key)
	file2.write('\n')
	for item in key:
		count+=1
		sum+=count

ave=sum/count

print('kolichestvo:',count, '  Summa:',sum,'  Average:',ave)
