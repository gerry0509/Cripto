import fileinput
lines=[]
suma=0
flotante=0
for line in fileinput.input():
	if '.' in line:
		flotante=1;	
	lines.append(line)
	suma=suma+float(line)
if flotante=1:
	print(suma)
else:
	print(int(suma))
