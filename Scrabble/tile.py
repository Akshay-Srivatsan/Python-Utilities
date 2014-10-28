class Tile(object):
	
	def __init__(self, letter, value):
		self.letter = letter
		self.value = value
		self.active = False
	def __str__(self):
		return self.letter
	def setLoc(self, row, col):
		self.row = row
		self.col = col