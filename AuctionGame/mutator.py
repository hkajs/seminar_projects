import sys
import random

mutateProb = 0.07
genNum = int(sys.argv[1])

# Read the gene sequence for this bot from a file, return as array
def readGenes(genNum, geneID):
	fileName = "genes\\gen_" + str(genNum) + "\\" + str(geneID)
	geneFile = open(fileName, "r")
	ar = []
	for i in range(0, 14):
		ar.append(float(geneFile.readline()))
	return ar
# readGenes(..)

# Writes a gene sequence from an array to a file
def writeGenes(genNum, geneID, genes):
	fileName = "genes\\gen_" + str(genNum) + "\\" + str(geneID)
	geneFile = open(fileName, "w")
	for gene in genes:
		geneFile.write(str(gene) + "\n")
# writeGenes(..)

# Mutates each gene in the gene sequence by a value between -0.5 and 0.5 with a probability of prob
def mutate(genes, prob):
	res = []
	for gene in genes:
		if random.random() < prob:
			res.append(gene + random.random() - 0.5)
		else:
			res.append(gene)
	return res
# mutate(genes)

# Reads the fitness from each member of the given generation and dumps it all into an array, which is then returned, index beginning at 1 (0 has fitness -1)
def readFitness(genNum):
	res = [-1]
	for i in range(1, 11):
		fileName = "fitness\\gen_" + str(genNum) + "\\" + str(i)
		fitFile = open(fileName, "r")
		res.append(int(fitFile.readline()))
	# for each individual
	return res
# readFitness(..)

# creates two offspring from sequence 1 and sequence 2, returns them in a list (which is a list of two lists)
# this is done by crossing over, then mutating each child's genome with small probability
def crossOver(seq1, seq2):
	cutLocation = random.randint(2, 13)
	child1 = seq1[:cutLocation]
	child1.extend(seq2[cutLocation:])
	child2 = seq2[:cutLocation]
	child2.extend(seq1[cutLocation:])
	child1 = mutate(child1, mutateProb)
	child2 = mutate(child2, mutateProb)
	return [child1, child2]
# crossOver(..)

fitnesses =  readFitness(genNum)
tmpfit = list(fitnesses) # shallow copy
mostFit = []
mostFit.append( readGenes(genNum, fitnesses.index(max(tmpfit)) ) )
tmpfit.remove(max(tmpfit))
mostFit.append( readGenes(genNum, fitnesses.index(max(tmpfit)) ) )
tmpfit.remove(max(tmpfit))
mostFit.append( readGenes(genNum, fitnesses.index(max(tmpfit)) ) )
tmpfit.remove(max(tmpfit))
mostFit.append( readGenes(genNum, fitnesses.index(max(tmpfit)) ) )
tmpfit.remove(max(tmpfit))

# mostFit is now the gene sequences of the most fit members of the generation, in order starting with the most fit

# The two most fit members of the current generation will join the next generation unchanged
writeGenes(genNum + 1, 1, mostFit[0])
writeGenes(genNum + 1, 2, mostFit[1])

for i in range(1, 5):
	parent1 = random.randint(0, 3)
	parent2 = random.randint(0, 3)
	# Yeah I know it's terrible, but for a list of fixed size 4 it is both more readable and easier to implement
	while parent1 == parent2:
		parent2 = random.randint(0, 3)
	children = crossOver(mostFit[parent1], mostFit[parent2])
	writeGenes(genNum + 1, (2*i) + 1, children[0])
	writeGenes(genNum + 1, (2*i) + 2, children[1])
	
	
	
	
	
	
	
	

