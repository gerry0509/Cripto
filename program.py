import fileinput
lines=[]
suma=0
for line in fileinput.input():
	lines.append(line)
	suma=suma+float(line)
print(suma)
