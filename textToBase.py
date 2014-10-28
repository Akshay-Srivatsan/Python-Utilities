
#NOTE: DOES NOT WORK ABOVE ~BASE 30

def numberToBinary(number):
	converted = ""
	largestPow = 0
	while 2**largestPow < number:
		largestPow += 1
	
	currentPow = largestPow
	while currentPow > 0:
		temp = number - 2**(currentPow - 1)
		if temp >= 0:
			converted += "1"
			number = temp
		else:
			converted +=  "0"
		currentPow -= 1
	return converted

def numberToBase(number, base):
	converted = ""
	largestPow = 0
	while base**largestPow < number:
		largestPow += 1
	
	currentPow = largestPow
	while currentPow > 0:
		if number - base**(currentPow - 1) >= 0:
			coefficient = 0
			while number - coefficient*(base**(currentPow - 1)) >= 0:
				coefficient += 1
			coefficient -= 1
			converted += charForNumInBase(coefficient)
			number -= coefficient*(base**(currentPow - 1))
		else:
			converted += "0"
		currentPow -= 1
	return converted

def charForNumInBase(num):
	if num < 10:
		return "" + str(num)
	else:
		return chr(ord('a') + (num - 10))
		
def stringToBase(word, base):
	temp = ""
	for letter in word:
		temp += numberToBase(ord(letter), base) + " "
	return temp

word = raw_input("Word to encode: ")
print stringToBase(word, 16)
print stringToBase(word, 8)
print stringToBase(word, 2)







