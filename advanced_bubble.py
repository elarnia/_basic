#!C:\Python34\python.exe

## advanced_bubble.py
## A program providing an OOP solution to the bubble sort.
## Sorts lists stored in arrays in ascending order.
## Author: Samuel Patrick
## Date: 9/13/16

import random

def generator():
    MAX_SEED = 10**10
    mynum = random.randint(0,MAX_SEED)
    return mynum

def bsort(data):
	size = len(data)
	sorted = False
	swaps = 0
	
	while sorted == False:
		position = 0
		sorted = True
	
		#compare all the elements in the list
		while position < (size-1):
			if data[position] > data[position+1]:
				temp = data[position]
				data[position] = data[position+1]
				data[position+1] = temp
				swaps += 1
				sorted = False
		
			position = position + 1
	return swaps
	
#__main__

#Seed the random number generator
random.seed(a=None, version=2)

ans = True
testA = []

for i in range(10):
	testA.append(generator()%1000)

print('Random list: ', end = " ") 
for each in testA:
	print(each, end = " ")
print()
	
swaps = bsort(testA)

print('Sorted list: ', end = " ") 
for each in testA:
	print(each, end = " ")
print()
print('Number of swaps: ', swaps)
print()

while ans == True:
	print('Please type a list to be sorted. Items should be seperated by a space.')
	user = input('(e.g. 1 2 3; a b c; boy cat dog): ')
	listU = user.split()
	swaps = bsort(listU)
	
	print('Sorted list: ', end = " ") 
	for each in listU:
		print(each, end = " ")
	print()
	print('Number of swaps: ', swaps)
	print()
	
	again = input('Would you like to try another list? (y/n): ')
		
	if again == 'n' or again == 'N':
		print('Thanks for sorting.')
		ans = False
	elif again == 'y' or again == 'Y':
		ans = True
	else:
		print('Invalid input. Ya done.')
		ans = False