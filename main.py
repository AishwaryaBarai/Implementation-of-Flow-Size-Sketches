import random
import sys
from math import log

numBitmap = 500000
numVirtual = 500
random500 = random.sample(range(0, sys.maxsize), numVirtual)
hashRand = random.randint(0, sys.maxsize)
sys.stdout  =  open("VirtualBitmapSpread.txt","w")


with open("project4input.txt") as fp: 
    
    Lines = fp.readlines() 
    numFlows = int (Lines[0])

    physicalBitMap = [0 for _ in range(numBitmap)]
    flowIds = random.sample(range(0, sys.maxsize), numFlows)

    for i in range(1, len(Lines)):
      a, b = Lines[i].split()
      randomFlows = random.sample(range(0, sys.maxsize), int(b))

      for randomVal in randomFlows:
        physicalBitMap [ (random500[(randomVal ^ hashRand) % numVirtual] ^ flowIds[i-1]) % numBitmap] = 1

vb = (numBitmap - sum(physicalBitMap)) / numBitmap
logvb = log(vb)

for fid in flowIds:
  zeros = 0
  for randomVal in random500:
    if physicalBitMap[(randomVal ^ fid) % numBitmap] == 0:
      zeros += 1
  vf = zeros / numVirtual
    
  spread = numVirtual * ( logvb - log(vf) )
  print(1 if spread < 1 else spread)


