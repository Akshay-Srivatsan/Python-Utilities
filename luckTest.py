from random import randint

numTries = int(raw_input('How many run throughs?:'))
chancePerGen = int(raw_input('What chance do you want to have to get a match(1 in x):'))
chance = 100* (1.0 - (1.0/(float(chancePerGen)))**(float(numTries)))
lastNum = randint(1, chancePerGen)
didMatch = False

for i in range(1, numTries):
	num = randint(1, chancePerGen)
	if num == lastNum:
		didMatch = True
		print "Congratulations you had a " + str(chance) + '%' + ' chance of this happening'
	lastNum = num

if not didMatch:
	print 'This had a ' + str(1 - chance) + '%' + ' chance of happening'