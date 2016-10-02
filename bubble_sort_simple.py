#!C:\Python34\python.exe

## bubble_sort.py
## A program providing a non OOP solution to the bubble sort.
## Sorts lists in ascending order.
## Author: Samuel Patrick
## Date: 9/13/16

#Counter to track the swaps
swaps = 0
#Marker for the position in the list
position = 0
#Variable for swaps
temp = 0
#User input
user_in = "y"
#Flag to tell if the list is sorted
sorted = False

#lists to be sorted
testA = [1,3,4,7,2,5]
testB = [1,2,3,4,5]
testC = [5,4,3,2,1]
testD = [10,4,-6,2,15,-2]
testE = ['b','i','n','g','o']
user = [0,0,0,0,0]

while sorted == False:
	position = 0
	sorted = True
	
	#compare all the elements in the list
	while position < 5:
		if testA[position] > testA[position+1]:
			temp = testA[position]
			testA[position] = testA[position+1]
			testA[position+1] = temp
			swaps = swaps + 1
			sorted = False
		
		position = position + 1

print ("List A:", end=" ")		
#python cheats when it comes to lists
for each in testA:
	print (each, end=" ")

print ()
print ("swaps =", swaps, sep=" ")
swaps = 0
sorted = False

while sorted == False:
	position = 0
	sorted = True
	
	#compare all the elements in the list
	while position < 4:
		if testB[position] > testB[position+1]:
			temp = testB[position]
			testB[position] = testB[position+1]
			testB[position+1] = temp
			swaps = swaps + 1
			sorted = False
		
		position = position + 1

print ("List B:", end=" ")
#python cheats when it comes to lists		
for each in testB:
	print (each, end=" ")

print ()
print ("swaps =", swaps, sep=" ")
swaps = 0
sorted = False

while sorted == False:
	position = 0
	sorted = True
	
	#compare all the elements in the list
	while position < 4:
		if testC[position] > testC[position+1]:
			temp = testC[position]
			testC[position] = testC[position+1]
			testC[position+1] = temp
			swaps = swaps + 1
			sorted = False
		
		position = position + 1

print ("List C:", end=" ")
#python cheats when it comes to lists		
for each in testC:
	print (each, end=" ")

print ()
print ("swaps =", swaps, sep=" ")
swaps = 0
sorted = False

while sorted == False:
	position = 0
	sorted = True
	
	#compare all the elements in the list
	while position < 5:
		if testD[position] > testD[position+1]:
			temp = testD[position]
			testD[position] = testD[position+1]
			testD[position+1] = temp
			swaps = swaps + 1
			sorted = False
		
		position = position + 1

print ("List D:", end=" ")
#python cheats when it comes to lists		
for each in testD:
	print (each, end=" ")

print ()
print ("swaps =", swaps, sep=" ")
swaps = 0
sorted = False

while sorted == False:
	position = 0
	sorted = True
	
	#compare all the elements in the list
	while position < 4:
		if testE[position] > testE[position+1]:
			temp = testE[position]
			testE[position] = testE[position+1]
			testE[position+1] = temp
			swaps = swaps + 1
			sorted = False
		
		position = position + 1

print ("List E:", end=" ")
#python cheats when it comes to lists		
for each in testE:
	print (each, end=" ")

print ()
print ("swaps =", swaps, sep=" ")
swaps = 0
sorted = False

#loop to get user input and sort it
while user_in == 'y' or user_in == 'Y':
	user[0] = input('Please input the first number: ')
	user[1] = input('Please input the second number: ')
	user[2] = input('Please input the third number: ')
	user[3] = input('Please input the fourth number: ')
	user[4] = input('Please input the fifth number: ')
	
	while sorted == False:
		position = 0
		sorted = True
	
		#compare all the elements in the list
		while position < 4:
			if user[position] > user[position+1]:
				temp = user[position]
				user[position] = user[position+1]
				user[position+1] = temp
				swaps = swaps + 1
				sorted = False
		
			position = position + 1

	print ("User List:", end=" ")
	#python cheats when it comes to lists		
	for each in user:
		print (each, end=" ")

	print ()
	print ("swaps =", swaps, sep=" ")
	swaps = 0
	sorted = False
	
	user_in = input('Enter another list? Y/N: ')
