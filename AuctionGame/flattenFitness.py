import sys

gen = sys.argv[1]

for i in range(1, 11):
	fileName = "fitness\\gen_" + gen + "\\" + str(i)
	fitFile = open(fileName, "r")
	num = 0
	for line in fitFile.readlines():
		if line != "":
			num = num + int(line)
	fitFile = open(fileName, "w")
	fitFile.write(str(num))