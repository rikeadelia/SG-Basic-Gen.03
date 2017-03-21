data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

teks = readData(data1)
output = []
what = ''
for each in teks:
	if(each == 'I') or (each == 'and') or (each == 'you') or (each == 'The'):
		what = '*'*len(each)
	else:
		what = each
	output.append(what)


print (" ".join(output))