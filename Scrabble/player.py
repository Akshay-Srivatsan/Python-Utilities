from random import randint

class Player(object):
		
	def getInitialTilesFromBank(self, wordBank):
		activeTiles = []
		for i in range(1, 8):
			num = randint(0, len(wordBank)-1)
			activeTiles += [wordBank[num]]
			wordBank.pop(num)
		return activeTiles
	
	def __init__(self, wordBank, maxTiles, name):
		self.name = name
		self.tiles = self.getInitialTilesFromBank(wordBank)
		self.score = 0
		self.maxTiles = maxTiles
	
	def getNewTiles(self, wordBank):
		newTiles = []
		numGet = self.maxTiles - len(self.tiles)
		for i in range(0, numGet):
			num = randint(0, len(wordBank)-1)
			newTiles += [wordBank[num]]
			wordBank.pop(num)
		self.tiles += newTiles