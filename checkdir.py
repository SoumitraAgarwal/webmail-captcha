import os

dirs = os.listdir("Individuals/")
empty = []

for item in dirs:
	if(len(os.listdir("Individuals/"+item))==0):
		empty.append(item)

print(empty)