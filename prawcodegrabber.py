import praw

initialStaticCodeChars = 'A05V'
codeLen = 16
subreddits = ['nintendo', '3ds']
subreddits = reduce(lambda a, b: a + '+' + b, subreddits)


def pullCommentCode(comment):
	text = comment.body
	codes = []
	while initialStaticCodeChars in text:
		index = text.index(initialStaticCodeChars)
		code = text[index:index+codeLen]
		codes += [code]
		text = text[:index] + text[index + codeLen:]
	return codes

r = praw.Reddit(user_agent='comment watcher')
	
for comment in praw.helpers.comment_stream(r, subreddits, limit=1, verbosity=1):
	codes = pullCommentCode(comment)
	for code in codes:
		print code