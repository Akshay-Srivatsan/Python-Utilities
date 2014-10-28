#!/usr/bin/python
from bigfloat import *
def run():
	calc();
	response = raw_input('Again?\n')
	while(response == 'yes'):
		calc()
		response = raw_input('Again?\n')
	while(response == 'loop'):
		calc()
def calc():
	numPeople = BigFloat(raw_input('Enter the number of people in the group:\n'));
	if(numPeople > 0):
		probability = BigFloat('1.0')
		while(numPeople > 0):
			probability = probability * (1-(numPeople/366))
			numPeople = numPeople - 1
		print (1 - probability) * 100
	elif(numPeople > 366):
		print 100.0
	else:
		print 0.0
precision(1000)
run()