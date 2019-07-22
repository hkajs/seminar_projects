import sys
from random import shuffle
from random import randint

# Written by Charles Zhang and Anthony Schalhoub
# November 2016
# Problem Solving with Professor Dennis Shasha

print("Please enter your input file's name.")

filename = input()
file = open(filename, 'r')

# This flag marks which part of the file we're reading (treatment, control)
flag = 0

treatment = []
control = []

# Read the file
for line in file:
	if line[0] == '>':
		flag = flag + 1
	elif flag == 1:
		treatment.extend(line.strip().split(' '))
	elif flag == 2:
		control.extend(line.strip().split(' '))
# for line in file

# Convert our lists into integer lists
treatment = [int(x) for x in treatment]
control = [int(x) for x in control]
# Conversion

# Calculates the significance of results
def sig(treatment, control):
	avgt = sum(treatment) / float(len(treatment))
	avgc = sum(control) / float(len(control))
	avgdif = abs(avgt - avgc)

	respool = treatment[:]
	respool.extend(control)
	# respool is our pool for resampling, it contains the total contents of treatment and control

	fcount = 0
	# fcount will be the number of times in which our random results are at least as significant as the original
	for i in range (1, 10000):
		shuffle(respool)
		newt = respool[0:len(treatment)]
		newc = respool[-len(control):]
		navgt = sum(newt)/float(len(newt))
		navgc = sum(newc)/float(len(newc))
		navgdif = abs(navgt - navgc)
		if navgdif >= avgdif:
			fcount = fcount + 1
	# i in range (1, 10000)

	alpha = fcount/10000
	return alpha
# sig(..)

# Calculates the x% confidence interval of the difference between the averages of treatment and control groups
def conf(treatment, control, x):
	diffs = []
	for i in range(1, 10000):
		newt = []
		for j in range(1, len(treatment)):
			newt.append(treatment[randint(0, len(treatment) - 1)])
		# once for every term in treatment
		newc = []
		for j in range(1, len(control)):
			newc.append(control[randint(0, len(control) - 1)])
		# once for every term in control
		navgt = sum(newt)/float(len(newt))
		navgc = sum(newc)/float(len(newc))
		diffs.append( navgt - navgc )
	# i in range (1, 10000)
	edge = (int)((100 - x) / 2) * 100
	diffs.sort()
	return [diffs[edge], diffs[len(diffs) - edge]]
# conf(..)

def sigtest(treatment, control):
        pvalue = sig(treatment, control)
        if sig(treatment, control) <= 0.05:
                return pvalue
        else:
                while pvalue > 0.05:
                        for x in range(0,int(len(treatment)/2)):
                                treatment.append(treatment[randint(0, len(treatment) - 1)])
                                control.append(control[randint(0, len(control) - 1)])
                        pvalue = sig(treatment, control)
                return pvalue


print("The original P-Value is equal to " + str(sig(treatment, control)))
print("The 90% confidence interval of the effects of the treatment is given by \n        " + str(conf(treatment, control, 90)))
print("Wait a moment...")
print("The new P-Value is equal to " + str(sigtest(treatment, control)) + " and the new group size is " + str(len(treatment))) 








