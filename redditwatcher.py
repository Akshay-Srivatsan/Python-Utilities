import urllib2
import time
import simplejson
import webbrowser

subreddit = 'nintendo'
def getNewestData():
	hdr = { 'User-Agent' : 'reddit watcher bot' }
	req = urllib2.Request('http://reddit.com/r/' + subreddit + '/new.json', headers=hdr)
	opener = urllib2.build_opener()
	f = opener.open(req)
	data = simplejson.load(f)
	return data['data']['children'][0]['data']


oldData = getNewestData()
newData = oldData

while True:
	newData = getNewestData()
	if(newData['url'] != oldData['url']):
		webbrowser.open_new(newData['url'])
	
	oldData = newData
	time.sleep(5)