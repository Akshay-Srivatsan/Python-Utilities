wordFile = open('/usr/share/dict/words')
line = wordFile.readline()
words = []
while line != '':
	words += [line]
	line = wordFile.readline()[:-1]

addedLengths = 0;
numWords = len(words);
for word in words:
	addedLengths += len(word)
print addedLengths
print addedLengths/numWords