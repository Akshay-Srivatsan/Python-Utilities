import os
import sys

#WARNING
#IT IS IMPERATIVE TO NOTE THAT THIS WILL DELETE ANY
#FILE THAT APPEARS TO FALL WITHIN THE CONFINES OF THE OSX
#AUTOMATED NAMING OF DUPLICATE DOWNLOADED FILES
#ANY TWO FILES WITH MATCHING STRINGS BEFORE ANY '(' IN THE FILE
#(SUCH AS 'example.txt'

def adjustedName(name):
	if '(' in name:
		return name[:name.find('(') - 1] + getExtension(name)
	return name
def getExtension(filename):
	lastIndex = 0
	for i in range(0, len(filename)):
		if filename[i] == '.':
			lastIndex = i
	return filename[lastIndex:]
def uniqueScrubedNames(directory):
	scrubedNames = []
	for filename in os.listdir(directory):
		adjusted = adjustedName(filename)
		if not adjusted in scrubedNames:
			scrubedNames += [adjusted]
	return scrubedNames
def deleteRepeats(directory):
	unique = uniqueScrubedNames(directory)
	toRemove = []
	print 'UNIQUE: ' + str(unique)
	for filename in os.listdir(directory):
		adjusted = adjustedName(filename)
		print 'filename: ' + filename
		print 'adjusted: ' + adjusted
		print 'unique: '
		if adjusted in unique:
			print 'is unique'
			unique.remove(adjusted)
		else:
			print 'isn\'t unique'
			toRemove += [filename]
	removeAll(directory, toRemove)
	
def removeAll(directory, toRemove):
	if directory[-1] != '/':
		directory += '/'
	for filename in toRemove:
		os.remove(directory + filename)
	
directory = raw_input("Enter Directory Path: ")
if directory != '':
	deleteRepeats(directory)