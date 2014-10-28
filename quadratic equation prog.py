import math

print 'Enter A...'
a = float(raw_input())

print 'Enter B...'
b = float(raw_input())

print 'Enter C...'
c = float(raw_input())

nB = (-1.0) * b
bS = math.pow(b, 2.0)
uRoot = bS - (4.0 * a * c)
rVal = math.sqrt(uRoot)
pAns = (nB + rVal) / (2.0 * a)
mAns = (nB - rVal) / (2.0 * a)
vX = (nB / (2.0 * a))
vY = (a * math.pow(vX, 2) + b * vX + c)
print 'Vertex is (' + str(vX) + ', ' + str(vY) + ')'

if(mAns != pAns):
 print 'x = ' + str(pAns) + ' or ' + str(mAns)
else:
 print 'x = ' + str(pAns)
 
class quadraticEquation(object):

 def __init__(self, a0, b0, c0):
  setattr(self, 'a', a0)
  setattr(self, 'b', b0)
  setattr(self, 'c', c0)
  
  nB = (-1) * b
  bS = math.pow(b, 2.0)
  uRoot = bS - (4.0 * a * c)
  rVal = math.sqrt(uRoot)
  pAns = (nB + rVal) / (2.0 * a)
  mAns = (nB - rVal) / (2.0 * a)
  setattr(self, 'mAns', mAns)
  setattr(self, 'pAns', pAns)
  
  vX = (nB / (2.0 * a))
  setattr(self, 'vX', vX)
  
  vY = (a * math.pow(vX, 2) + b * vX + c)
  setattr(self, 'vY', vY)
  
 
 def getVertex()
  return Point(vX, vY)

 def getSolutions():
  return {getattr(self, vX), getattr(self, vY)}
  
 