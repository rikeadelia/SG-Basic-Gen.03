data1 = "Data1.txt"
data2 = "Data2.txt"

def readData(data1):
	x = []
	with open(data1) as data :
	    for line in data :
		    x = line.split()
	return x

teks1 = readData(data1)
teks2 = readData(data2)
what = ''
output = []

for each1 in teks1:
	for each2 in teks2:
		if(each1 == each2):
			what = each1
	if(what not in output):
		output.append(each1)

print(output)