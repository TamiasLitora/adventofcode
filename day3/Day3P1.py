#day 3
#the file containing data
inputFile = open("day3/input", "r")

#read in file to list
file = inputFile.readlines()
#custom length bitcounts, not required but adaptable!
bitCount= [0] * len(file[0].strip())
secondaryCount= [0] * len(file[0].strip())
countTotal= 0

for line in file:
    countTotal +=1
    for i in range(len(bitCount)):
        #increments spot if that lines bit position is 1
        if int(list(line) [i]) == 1:
            bitCount[i] += 1

#convert count into correct format, and populate secondaryCount
for i in range(len(bitCount)):
    if bitCount[i] > (countTotal/2):
        bitCount[i] = 1
        secondaryCount[i]=0
    else:
        bitCount[i] = 0
        secondaryCount[i]=1

#changing numbers to decimal
gammarate =  ''.join(str(i) for i in bitCount)
epsilonrate = ''.join(str(i) for i in secondaryCount)
gammarate = int(gammarate, 2)
epsilonrate = int(epsilonrate, 2)

print("%s number of items, with a final bit setup of %s "% (countTotal, bitCount))
print("%s gammarate, %s epsilonrate, %s powerconsumption"% (gammarate, epsilonrate, (gammarate*epsilonrate)))
#for line in file:
