import urllib2
import time
import simplejson
import webbrowser

subreddit = ''
def getNewestPost():
	hdr = { 'User-Agent' : 'nintendo watcher bot' }
	req = urllib2.Request('http://reddit.com/r/nintendo/new.json', headers=hdr)
	opener = urllib2.build_opener()
	f = opener.open(req)
	data = simplejson.load(f)
	return data['data']['children'][0]['data']
	
def getNewestComment():
	hdr = { 'User-Agent' : 'nintendo watcher bot' }
	req = urllib2.Request('http://www.reddit.com/r/nintendo/comments.json', headers=hdr)
	opener = urllib2.build_opener()
	f = opener.open(req)
	data = simplejson.load(f)
	return data['data']['children'][0]['data']['body']

def getComments(numComments):
	hdr = { 'User-Agent' : 'watcher bot' }
	req = urllib2.Request('http://www.reddit.com/r/nintendo/comments.json', headers=hdr)
	opener = urllib2.build_opener()
	f = opener.open(req)
	data = simplejson.load(f)
	comments = data['data']['children']
	commentBodies = []
	for num in range(0, numComments):
		commentBodies += [comments[num]['data']['body']]
	return commentBodies

def pullCommentCode(comment):
	text = comment
	codes = []
	while "A05V" in text:
		index = comment.index('A')
		code = comment[index:index+16]
		codes += [code]
		text = text[:index] + text[index + 16:]
	return codes

def removeOldComments(newComments, oldComments):
	onlyNewComments = []
	for comment in newComments:
		isNew = True
		for old in oldComments:
			if comment == old:
				isNew = False
				print comment[:10] + ' is the same as ' + old[:10]
		if isNew:
			onlyNewComments+=[comment]
	print onlyNewComments
	return onlyNewComments
	
def pullSubmissionCode(submission):
	text = submission
	codes = []
	while 'A05V' in text:
		index = submission.index('A05V')
		code = submission[index:index+16]
		codes += [code]
		text = text[:index] + text[index + 16:]
	return codes

def printNewCodes(newPost, oldPost, newComments, oldComments):
	codes = []
	
	if(newPost['url'] != oldPost['url']):
		if oldPost['selftext'] != None:
			codes += pullSubmissionCode(oldPost['selftext'])
				
	newComments = removeOldComments(newComments, oldComments)
	for comment in newComments:
		codes += pullSubmissionCode(comment)
	
	for code in codes:
		print code
		
	
	
commentsToGrab = 5
secondsToSleep = 5
oldPost = getNewestPost()
newPost = oldPost
oldComments = getComments(commentsToGrab)
newComments = oldComments

while True:
	newPost = getNewestPost()
	#newComments = getComments(5)
	
	#printNewCodes(newPost, oldPost, newComments, oldComments)

	print getNewestComment()[:5]

	oldComments = newComments
	oldPost = newPost
	time.sleep(secondsToSleep)
	
	
	
	
	
	
	
	
	
	
	
	