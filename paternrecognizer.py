def allPossible(string, minLen):
	possible = []
	for i in range(0, len(string)/2):
		for i2 in range(i + (minLen-1), len(string)/2):
			possible += [string[i:i2+1]]
	return possible

def numOccurences(string, minLen, minOccurences):
	keys = allPossible(string, minLen)
	dictS = {}
	for key in keys:
		dictS[key] = 0
		for i in range(0, len(string)):
			for i2 in range(i, len(string)/2):
				if key == string[i:i2+1]:
					dictS[key] += 1
	filter(lambda key: dictS[key] >= minOccurences, dictS)
	return dictS
	
def top(num, dictS):
	top = []
	for key in dictS:
		if len(top) < num:
			top+=[key]
		else:
			for i in top:
				if dictS[key] > dictS[i] and key not in top:
					top.remove(i)
					top += [key]
	topD = {}
	for s in top:
		topD[s] = dictS[s]
	return topD

def sortedKeys(dictS):
	keylst = []
	for key in dictS:
		keylst += [key]
	sortedlst = []
	for i in range(0, len(keylst)):
		key = getLargest(keylst, dictS)
		sortedlst += [key]
		keylst.remove(key)
	return sortedlst
		
		
def getLargest(keylst, dictS):
	largest = ''
	for key in keylst:
		if largest == '':
			largest = key
		elif dictS[key] > dictS[largest]:
			largest = key
	return largest
	
top5 = top(5,numOccurences('ashdfuowehioausdngioabsdgoaxhzdiabdiougabsoidgbaisdbgoausbdgo8axdbgoasudvoagaweoirghaosidngiljxcznvouinrutoasmgdt02e82eapndfuaen4qeirjhsoid', 2, 2))
print numOccurences('ashdfuowehioausdngioabsdgoaxhzdiabdiougabsoidgbaisdbgoausbdgo8axdbgoasudvoagaweoirghaosidngiljxcznvouinrutoasmgdt02e82eapndfuaen4qeirjhsoid', 2, 2)













