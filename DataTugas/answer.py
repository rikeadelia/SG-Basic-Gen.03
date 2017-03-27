data1 = "DataSet.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x
	

teks1 = readData(data1)
arr = []
idx = []
word = (teks1[0])[0].upper() + (teks1[0])[1:]
teks1[0] = word
for i, each in enumerate(teks1):
	#print (each)
	if(each[len(each)-1] == ".") and (i != len(teks1)-1):
		word = (teks1[i+1])[0].upper() + (teks1[i+1])[1:]
		teks1[i+1] = word
	if(each.isdigit()):
		arr.append(each)
		idx.append(i)

j=len(arr) - 1
for each in idx:
	teks1[each] = arr[j]
	j-=1


# print (arr)
# print (idx)
print (" ".join(teks1))