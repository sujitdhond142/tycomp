# Assignment no 2

def countChars(text,character,ignore_case=True):
	# returns no of character occurance in string with or without case sensitivity
	if ignore_case:
		text=text.lower()
		character=character.lower()
	no=0
	for t in text:
		if character==t:
			no=no+1
	print("No of ",character,"in ",text," : ",no)

def getMinMax(arr):
	# get min and max value in array
	min=arr[0]
	max=arr[0]
	for i in range(0,len(arr)):
		if arr[i]<min:
			min=arr[i]
		if arr[i]>max:
			max=arr[i]
	return min,max

def listOperations():
	#operations on list
	arr=[6,7,2,4,5]
	print("List created")
	print(arr)
	print("No of items in list : ",len(arr))
	arr.append(3)
	print("3 appended at end of list")
	print(arr)
	arr.remove(4)
	print("4 deleted from list")
	print(arr)

def tupleOperations():
	# operations on tuples
	rgb=(123,45,67)
	print("color as tuple : ",rgb)
	print("Changing value of tuple")
	try:
		rgb[0]=34
	except TypeError as e:
		print("Error :",e)
	rgb2=77,88,99
	print("Another color as tuple : ",rgb2)
	red,green,blue=rgb2
	print("Value of red color : ",red)
	print("Value of green color : ",green)
	print("Value of blue color : ",blue)

def dictOperations():
	# Operations on dictionaries
	tel={'harish':4098,'vihaan':4139}
	print("dictionay created")
	print(tel)
	tel['chetana']=4127
	print("chetana added to dictionay")
	print(tel)
	print("Marks of harish : ",tel['harish'])
	tel.pop('vihaan')
	print("vihaan deleted from dictionary")
	print("Names from dictionaries : ",tel.keys())
	print("Marks from dictionaries : ",tel.values())
	test = 'chetana' in tel
	print("Is chetana in dictionary : ",test)

ch="Y"
while (ch=="Y" or ch=="y"):
    # program menu
	print("Program menu")
	print("1.Built-in functions")
	print("2.Functions with default arguments")
	print("3.Functions with multiple return values")
	print("4.Lists")
	print("5.Tuples")
	print("6.Dictionaries")

	print("\nEnter yout choice : ")
	n=int(input())

	if n==1:
        # Built-in functions
		# int() function will convert value to integer
		# str() function will convert value to string
		x=int(input("Enter any number "))
		y=str(input("Enter a string "))
		print("Entered number : ",x)
		print("Entered string : ",y)
	elif n==2:
		# functions with default arguments
		text="some TEXT"
		character="e"
		countChars(text,character)
		countChars(text,character,True)
		countChars(text,character,False)
	elif n==3:
		# function with multiple return values
		arr=[7,8,3,2,5,6]
		print("Given array : ",arr)
		min,max=getMinMax(arr)
		print("min : ",min," max : ",max)
	elif n==4:
		# perform operation on tuples
		listOperations()
	elif n==5:
		# perform operation on tuples
		tupleOperations()
	elif n==6:
		# perform operation on dectionaries
		dictOperations()
	else:
        # Invalid choice
		print("wrong choice")

	print("Do you want to continue (y/n) ")
	ch=str(input())

#end of first while loop



