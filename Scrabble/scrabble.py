from tile import Tile
from player import Player
from drawing import *
from button import Button
from random import randint

currentPlayer = 0
activeTiles = []
letterBank = []
players = []
moveTiles = []
#you want to store it in a dictionary because it is easier to check for words
grid = {}
MAX_TILES = 7
NUM_COL = 15
NUM_ROW = 15
TILE_WIDTH = 38
HEIGHT = 800
WIDTH = 600
rackX = 0
rackY = 0
rackLength = 0
rackHeight = 0
selected = None
universalFont = 'ComicSansMS'
moveButton = Button(WIDTH - 75, HEIGHT - 150, 50, 125, '#FFF2CC', 'Move', lambda:makeMove(), universalFont + ' 22')
cheatButton = Button(75, HEIGHT - 150, 50, 125, '#FFF2CC', 'Cheat', lambda: cheat(), universalFont + ' 22')
scrambleButton = Button(75, HEIGHT - 100, 50, 125, '#FFF2CC', 'Scramble', lambda: scrambleTiles(), universalFont + ' 22')
swapButton = Button(WIDTH - 75, HEIGHT - 100, 50, 125, '#FFF2CC', 'Swap', lambda: swapTile(), universalFont + ' 22')
forfeitButton = Button(WIDTH/2, HEIGHT - 20, 40, 125, 'red', 'Forfeit', lambda: forfeit(), universalFont + ' 22')
buttonList = [moveButton, cheatButton, scrambleButton, swapButton, forfeitButton]
numPlayers = 0
validWords = []
firstMove = True
centerPos = (NUM_ROW/2, NUM_COL/2)

letterAmounts = {'A': 9, 'B': 2, 'C': 2, 'D':4, 'E': 12, 'F': 2, 'G':3, 'H': 2, 'I': 
				 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N':6, 'O': 8, 'P': 2, 'Q': 1, 
				 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 
				 1, '_': 2}
letterValues = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 3, 'H': 4, 'I': 
				1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N':1, 'O': 1, 'P': 3, 'Q': 10, 
				'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 
				10, '_': 0}
wordMultipliers = {(0, 0): 3, (0,6): 3, (0, 14): 3, (1, 1): 2, (1, 13) : 2, (2, 2): 2, (2, 12): 1, (3, 3): 2, (3, 11): 2, (4, 4): 2, (4, 10): 2, (6, 0): 3, (6, 14): 3, (10, 4): 2, (10, 10): 2, (11, 3): 2, (11, 11): 2, (12, 2): 2, (12, 12): 2, (13, 1): 2, (13, 13): 2, (14, 0): 3, (14, 6): 3, (14, 14): 3}
letterMultipliers = {(3, 7): 2, (1, 9): 3, (9,5): 3, (6, 6): 2, (0, 3): 2, (8, 2): 2, (13, 5): 3, (9, 9): 3, (2, 6): 2, (14, 11): 2, (7, 3): 2, (11, 7): 2, (3, 0): 2, (14, 3): 2, (1, 5): 3, (5, 5): 3, (6, 12): 2, (5, 1): 3, (11, 0): 2, (6, 8): 2, (6, 2): 2, (2, 8): 2, (13, 9): 3, (0, 11): 2, (9, 1): 3, (9, 13): 3, (12, 6): 2, (11, 14): 2, (7, 11): 2, (8, 6): 2, (12, 8): 2, (5, 13): 3, (8, 8): 2, (3, 14): 2, (5, 9): 3, (8, 12): 2}

def getTileList():
	letters = []
	for letter in letterAmounts:
		for num in range(1, letterAmounts[letter] + 1):
			letters += [Tile(letter, letterValues[letter])]
	return letters
	
def initPlayers(numPlayers):
	askNames = raw_input("Do you want to input names?(Yes/No):\n")
	if askNames == 'Yes':
		askNames = True
	else:
		askNames = False
		
	global letterBank
	players = []
	for i in range(0, numPlayers):
		if askNames:
			name = raw_input('Who is player ' + str(i + 1) + '?:\n')
		else:
			name = str(i + 1)
		players += [Player(letterBank, MAX_TILES, name)]
	return players

def placeTile(row, col, tile):
	if(not((row, col) in grid)):
		global grid
		grid[(row, col)] = tile
		tile.row = row
		tile.col = col
		# global activeTiles
		# activeTiles += [tile]
	
def drawRack():
	length = 7 * (TILE_WIDTH + 2)
	startX =  WIDTH/2 - length/2
	startY = HEIGHT - 150
	
	global rackX
	global rackY
	global rackLength
	global rackHeight
	rackX = startX
	rackY = startY
	rackLength = length
	rackHeight = 50
	
	draw.rect(startX, startY, WIDTH/2 + length/2, HEIGHT - 100,  fill='#CC9900')
	drawPlayerTiles(startX, startY)

def forfeit():
	global numPlayers
	players.pop(currentPlayer % numPlayers)
	numPlayers-=1
	
def drawBoardTiles():
	global grid
	for key in  grid:
		tile = grid[key]
		startY = (TILE_WIDTH + 2) * tile.row
		startX = (TILE_WIDTH + 2) * tile.col
		endX = startX + TILE_WIDTH
		endY = startY + TILE_WIDTH
		draw.rect(startX, startY, endX, endY, fill='#FFF2CC')
		draw.text(startX + TILE_WIDTH/2, endY - TILE_WIDTH/2, text=tile.letter, font = universalFont + ' 24')
		draw.text(startX + 5*TILE_WIDTH/6, endY - TILE_WIDTH/4, text=tile.value, font = universalFont + ' 12')
		
def printList(listin):
	for i in range(0, len(listin)):
		print listin[i]

def swapTile():
	global letterBank
	global selected
	global currentPlayer
	if selected != None and len(letterBank) > 0:
		player = players[currentPlayer%numPlayers]
		letterBank += [selected]
		player.tiles.remove(selected)
		num = randint(0, len(letterBank) - 1)
		player.tiles += [letterBank[num]]
		currentPlayer+=1
		selected = None

def scrambleTiles():
	player = players[currentPlayer%numPlayers]
	tiles = player.tiles
	newTiles = []
	for num in range(0, len(tiles)):
		index = randint(0, len(tiles) - 1)
		tile = tiles[index]
		newTiles += [tile]
		tiles.remove(tile)
	player.tiles = newTiles
		

def drawPlayerTiles(rackStartX, rackStartY):
	player = players[currentPlayer%numPlayers]
	for num in range(0, len(player.tiles)):
		tile = player.tiles[num]
		if(tile.active == False):
			startX = rackStartX + num * (TILE_WIDTH + 2) + 2
			startY = rackStartY
			endX = startX + TILE_WIDTH
			endY = startY + TILE_WIDTH
			if(selected == tile):
				color = '#FFBF00'
			else:
				color = '#FFF2CC'
			draw.rect(startX, startY, endX, endY, fill=color)
			draw.text(startX + TILE_WIDTH/2, endY - TILE_WIDTH/2, text=tile.letter, font = universalFont + ' 22')
			draw.text(startX + 5*TILE_WIDTH/6, endY - TILE_WIDTH/4, text=tile.value, font = universalFont + ' 12')

def drawGame():
	draw.rect(0, 0, WIDTH, HEIGHT, fill = 'white', outline = 'white')
	drawGIF(300, 300, 'board.gif')
	drawRack()
	drawBoardTiles()	
	for button in buttonList:
		button.draw()
	draw.text(WIDTH/2, HEIGHT - 80, text = 'Player: ' + players[currentPlayer%numPlayers].name, font = universalFont + ' 24')
	draw.text(WIDTH/2, HEIGHT - 55, text = 'Score: ' + str(players[currentPlayer%numPlayers].score), font = universalFont + ' 20')

def makeMove():
	move = validMove()
	valid = move[0]
	if valid:
		word = move[1]
		global activeTiles
		global moveTiles
		if(word.find('_') != -1):
			newLetter = move[2]
			replaceSpaceTileWith(newLetter, moveTiles)
		activeTiles += moveTiles
		
		global players
		global currentPlayer
		global numPlayers
		player = players[currentPlayer%numPlayers]
		score = scoreWord(word)
		player.score = score
		print 'Points Gained: ' + str(score) + '\n'
		player.getNewTiles(letterBank)
		
		moveTiles = []
		currentPlayer += 1;
		drawGame()
		
def anyTileOnPos(pos, tiles):
	for tile in tiles:
		if (tile.row, tile.col) == pos:
			return True
	return False

def validMove():
	global firstMove
	if firstMove == True:
		if anyTileOnPos(centerPos,  moveTiles) == False:
			return False, ""
		firstMove = False
	for key in grid:
		tile = grid[key]
		if not isConnected(tile):
			return False, ""
	if len(moveTiles) > 0:
		sameRow = checkRow(moveTiles)
		sameCol = checkCol(moveTiles)
		if sameRow:
			connectedTiles = getConnectedTilesInRow(moveTiles[0])
			orderedTiles = getLeftToRight(connectedTiles)
			word = wordFromTiles(orderedTiles)
			if(word.find('_') != -1):
				valid = wordIsWord(word)
				if valid[0]:
					oldWord = valid[1]
					newWord = valid[2]
					newLetter = valid[3]
					return True, oldWord, newLetter
				return False, ""
			elif(not wordIsWord(word)):
				return False, word
		if sameCol:
			connectedTiles = getConnectedTilesInCol(moveTiles[0])
			orderedTiles = getTopToBottom(connectedTiles)
			word = wordFromTiles(orderedTiles)
			if(word.find('_') != -1):
				valid = wordIsWord(word)
				if valid[0]:
					oldWord = valid[1]
					newWord = valid[2]
					newLetter = valid[3]
					return True, oldWord, newLetter
				return False, ""
			elif(not wordIsWord(word)):
				return False, word
		if not sameRow and not sameCol:
			return False, ""
		return True, word
	return False, ""

def replaceSpaceTileWith(newLetter, tiles):
	for tile in tiles:
		if(tile.letter == '_'):
			tile.letter = newLetter
			
def wordIsWord(word):
	if(len(word) > 1):
		spaceIndex = word.find('_')
		if spaceIndex != -1:
			for num in range(0, 26):
				newLetter = chr(ord('A') + num)
				tempWord = word[:spaceIndex] + newLetter + word[spaceIndex + 1:]
				for listWord in validWords:
					if tempWord == listWord:
						return True, word, tempWord, newLetter
			return False, ""
		else:
			for listWord in validWords:
				if word == listWord:
					return True
		return False

def printTileLetters(tileList):
	for tile in tileList:
		print tile.letter	

def wordFromTiles(tiles):
	str = ""
	for tile in tiles:
		str += tile.letter
	return str
		
	
def getTopToBottom(tiles):
	highest = tiles[0]
	for tile in tiles:
		if(tile.row < highest.row):
			highest = tile
	
	ordered = []
	for num in range(0, len(tiles)):
		ordered += [grid[(highest.row + num, highest.col)]]
	return ordered

def getLeftToRight(tiles):
	#finds the furthest tile to the left
	furthestLeft = tiles[0]
	for tile in tiles:
		if tile.col < furthestLeft.col:
			furthestLeft = tile
	
	ordered = []
	for num in range(0, len(tiles)):
		ordered += [grid[(furthestLeft.row, furthestLeft.col + num)]]
	return ordered

def getConnectedTilesInRow(startTile):
	row = startTile.row
	col = startTile.col
	connected = []
	
	while(col >= 0 and (row, col) in grid):
		connected += [grid[(row, col)]]
		col -= 1
		
	col = startTile.col + 1
	while(col < NUM_COL and (row, col) in grid):
		connected += [grid[(row, col)]]
		col += 1
	return connected

def getConnectedTilesInCol(startTile):
	col = startTile.col
	row = startTile.row
	connected = []
	
	while(row >= 0 and (row, col) in grid):
		connected += [grid[row, col]]
		row -= 1

	row = startTile.row + 1
	while(row < NUM_ROW and (row, col) in grid):
		connected += [grid[(row, col)]]
		row += 1
	
	return connected

def checkRow(tiles):
	if len(tiles) > 1:
		row = tiles[0].row
		for tile in tiles:
			if tile.row != row:
				return False
		return True
	else:
		tile = tiles[0]
		right = (tile.row, tile.col + 1)
		left = (tile.row, tile.col - 1)
		if(left in grid or right in grid):
			return True
		return False
	
def checkCol(tiles):
	if len(tiles) > 1:
		col = tiles[0].col
		for tile in tiles:
			if tile.col != col:
				return False
		return True
	else:
		tile = tiles[0]
		above = (tile.row + 1, tile.col)
		below = (tile.row - 1, tile.col)
		if(above in grid or below in grid):
			return True
		return False

def isConnected(tile):
	row = tile.row
	col = tile.col
	if (row + 1, col) in grid:
		return True
	if (row - 1, col) in grid:
		return True
	if (row, col + 1) in grid:
		return True
	if (row, col - 1) in grid:
		return True
	
def canPlace(word, placedTile):
	index = word.find(placedTile.letter)
	if index != -1:
		upSpace = True
		downSpace = True
		rightSpace = True
		leftSpace = True
		for num in range(1, len(word[:index]) + 1):
			col = placedTile.col
			row = placedTile.row
			newCol = col - num
			newRow = row - num
			if (row, newCol) in grid or newCol < 0 or (row - 1, col) in grid or (row + 1, col) in grid:
				leftSpace = False
			if (newRow, placedTile.col) in grid or newRow < 0 or (row, col - 1) in grid or (row, col -1) in grid:
				upSpace = False
				
		for num in range(1, len(word[index:]) + 1):
			col = placedTile.col
			row = placedTile.row
			newCol = col + num
			newRow = row + num
			if (row, newCol) in grid or col >= NUM_COL or (row - 1, col) in grid or (row + 1, col) in grid:
				rightSpace = False
				
			if	(newRow, col) in grid or row >= NUM_ROW or (row, col - 1) in grid or (row, col -1) in grid:
				downSpace = False
		
		upDown = False
		leftRight = False
		if upSpace == True and downSpace == True:
			upDown = True
		if leftSpace == True and rightSpace == True:
			leftRight = True
		if upDown == True or leftRight == True:
			return True
	return False
		

def removeTile(tile):
	tile.active = False
	moveTiles.remove(tile)
	players[currentPlayer%numPlayers].tiles += [tile]
	grid.pop((tile.row, tile.col))
	

def handleMouseClick(x, y):
	if(x > rackX and x < rackX + rackLength and y < rackY + rackHeight
	   and y > rackY):
	   distanceFromStart = x - rackX
	   rackTiles = players[currentPlayer%numPlayers].tiles
	   tile = rackTiles[distanceFromStart / (TILE_WIDTH + 2) % len(rackTiles)]
	   if(tile.active == False):
		   global selected
		   selected = tile
	elif(x > 0 and x < 600 and y > 0 and y < 600):
		row = y / (TILE_WIDTH + 2)
		col = x / (TILE_WIDTH + 2)
		if selected != None and not((row, col) in grid):
			placeTile(row, col, selected)
			
			global players
			players[currentPlayer%numPlayers].tiles.remove(selected)
			
			global moveTiles
			moveTiles += [selected]
			
			global selected
			selected = None
		else:
			if((row, col) in grid):
				if grid[(row, col)] in moveTiles:
					removeTile(grid[(row, col)])
	else:
		for button in buttonList:
			if(x > button.x - button.width / 2 and x < button.x + button.width/2 
			   and y > button.y - button.height/2 and y <  button.y + button.height/2):
				button.method()
	drawGame()

def getNeighbors(tile):
	neighbors = []
	row = tile.row
	col = tile.col
	if (row, col+1) in grid:
		neighbors += [grid[(row, col+1)]]
	if (row, col - 1) in grid:
		neighbors += [grid[(row, col - 1)]]
	if (row + 1, col) in grid:
		neighbors += [grid[(row + 1, col)]]
	if (row - 1, col) in grid:
		neighbors += [grid[(row - 1, col)]]
	if (row + 1, col + 1) in grid:
		neighbors += [grid[(row + 1, col + 1)]]
	if (row - 1, col - 1) in grid:
		neighbors += [grid[(row - 1, col - 1)]]
	if (row + 1, col - 1) in grid:
		neighbors += [grid[(row + 1, col - 1)]]
	if (row - 1, col + 1) in grid:
		neighbors += [grid[(row - 1, col + 1)]]
	return neighbors

def cheat():
	possibleWords = []
	tileSet = players[currentPlayer%numPlayers].tiles
	stringLetters = wordFromTiles(tileSet)
	
	global validWords
	if(activeTiles == []):
		if stringLetters.find('_') != -1:
			for num in range(0, 26):
				spaceReplacement = chr(ord('A') + num)
				for word in validWords:
					newSet = stringLetters + spaceReplacement
					if subset(word, newSet):
						if subset(word, stringLetters):
							possibleWords += [word]
						else:
							indexOfReplacement = word.find(spaceReplacement)
							if indexOfReplacement == len(word) - 1:
								tileSpelling = word[:indexOfReplacement] + '_'
							else:
								tileSpelling = word[:indexOfReplacement] + '_' + word[indexOfReplacement + 1:]
							possibleWords += [tileSpelling]
		else:
			for word in validWords:
				if subset(word, stringLetters):
					possibleWords += [word]
	else:
		if stringLetters.find('_') != -1:
			for num in range(0, 26):
				spaceReplacement = chr(ord('A') + num)
				for key in grid:
					letter = grid[key].letter
					newSet = stringLetters + letter + spaceReplacement
					for word in validWords:
						if subset(word, stringLetters):
							possibleWords += [word]
						else:
							indexOfReplacement = word.find(spaceReplacement)
							if indexOfReplacement == len(word) - 1:
								tileSpelling = word[:indexOfReplacement] + '_'
							else:
								tileSpelling = word[:indexOfReplacement] + '_' + word[indexOfReplacement + 1:]
							possibleWords += [tileSpelling]
		else:
			for key in grid:
				letter = grid[key].letter
				for word in validWords:
					if subset(word, stringLetters + letter) and canPlace(word, grid[key]):
						possibleWords += [word]
	
	bestWord = findBestScore(possibleWords)
	print 'Word: ' + bestWord[0]
	print 'Score: ' + str(bestWord[1])
	autoPlaceWord(bestWord[0])
	
def autoPlaceWord(word):
	player = players[currentPlayer%numPlayers]
	rack = player.tiles
	tempWord = word
	print tempWord
	for tile in rack:
		index = word.find(tile.letter)
		if index != -1:
			if index == 0:
				tempWord = tempWord[index + 1:]
			tempWord = tempWord[:index] + tempWord[index + 1:]
		print tempWord
	print tempWord

def getWordsFromFile():
	wordFile = open('words.txt')
	line = wordFile.readline()
	words = []
	while line != '':
		words += [line]
		line = wordFile.readline()[:-1]
	return words

def findBestScore(wordList):
	bestScore = 0
	bestWord = ''
	for word in wordList:
		score = scoreWord(word)
		if score > bestScore:
			bestScore = score
			bestWord = word
	return (bestWord, bestScore)
	
def scoreWord(word):
	score = 0
	for letter in word:
		score += letterValues[letter]
	global wordMultipliers
	global letterMultipliers
	wordMultiplier = 1
	for tile in moveTiles:
		if (tile.row, tile.col) in wordMultipliers:
			wordMultiplier *= wordMultipliers[(tile.row, tile.col)]
		elif (tile.row,tile.col) in letterMultipliers:
			score += ((letterMultipliers[(tile.row, tile.col)]-1) * tile.value)
			print tile.value
	return score * wordMultiplier
		
def subset(s1, s2):
	for letter in s1:
		index = s2.find(letter)
		if index == -1:
			return False
		else:
			s2 = s2[:index] + s2[index + 1:]
	return True

def keyHandler(char):
	if(char == 'v'):
		print validMove()
	elif(char == 'c'):
		cheat()
	elif(char == 'm'):
		makeMove()

def main():
	global validWords
	validWords = getWordsFromFile()
	
	global numPlayers
	numPlayers = int(raw_input("How many players are there? (4 max):\n"))
	if numPlayers > 4:
		numPlayers = 4
	
	global letterBank
	letterBank = getTileList()
	
	global players
	players = initPlayers(numPlayers)
	
	# tile = None
	# for x in range(2, 10):
	# 	char = chr(ord('B') + x)
	# 	tile = Tile(char, letterValues[char])
	# 	print char
	# 	placeTile(4, x, tile)
	# 
	# con = getConnectedTilesInRow(tile)
	# print con
	# for t in con:
	# 	print t.letter
	# con = getLeftToRight(con)
	# print con
	# for t in con:
	# 	print t.letter
	newWindow(HEIGHT, WIDTH)
	
	drawGame()
	bindMouseClick(handleMouseClick)
	bindKeyChar(keyHandler)
	#cheat()
		
	
main()
draw.WINDOW.mainloop()