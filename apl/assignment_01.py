# Assignment no 1

ch="Y"
while (ch=="Y" or ch=="y"):
    # program menu
	print("Program menu")
	print("1.Find square root of no : ")
	print("2.Find area of rectangle : ")
	print("3.Swap two nos : ")
	print("4.data structures: list,dictonaries,tuples")
	print("5.Find no is even or odd")
	print("6.Largest among three no.s")
	print("7.Check if year is leap or not")
	print("8.Fibonacci Sequence")
	print("9.While loop")
	print("10.Prime no upto n nos:")
	print("11.Perform operations on word \"govenrmentcollege\" ")

	print("\nEnter any no. ")
	n=int(input())

	if n==1:
        # Square root of a number
		num = int(input("Enter your number "))
		print("Square root of no is :",(num**0.5))

	elif n==2:
        # Area of rectangle
		width = int(input("Enter width of rectangle : "))
		height = int(input("Enter height of rectangle : "))
		print("Area of rectangle is : ",(width*height))

	elif n==3:
        # Swap number
		a = int(input("Enter first no. : "))
		b = int(input("Enter second no. : "))
		c = a
		a=b
		b=c
		print("After swap")
		print("First no is : ",a)
		print("Second no is: ",b)

	elif n==4:
        # Data structures
		print("Data structure ")
		a=[1,"two",3]
		print("List ")
		print(a)
		b=(4,"five",6)
		print("Tuple")
		print(b)
		c={1:"one",2:"two",3:"three"}
		print("Dictionary")
		print(c)

	elif n==5:
        # Check if number is even or odd
		num=int(input("Enter number "))
		if num%2==0:
			print("Number is even ")
		else:
			print("Number is odd")

	elif n==6:
        # Geatest number among three numbers
		a=int(input("Enter first no : "))
		b=int(input("Enter second no : "))
		c=int(input("Enter third no : "))
		if a<b :
			if b<c:
				print("Greatest no is : ",c)
			else:
				print("Greatest no is : ",b)
		else :
			if a<c:
				print("Greatest no is : ",c)
			else:
				print("Greatest no is : ",a)

	elif n==7:
        # Check if year is leap year
		a=int(input("Enter year : "))
		if a%4==0:
			if a%400==0:
				print("Not a leap year")
			else:
				print("It's a leap year")	
		else:
				print("Not a leap year")

	elif n==8:
        # Fibonacci Series
		a=1
		b=1
		i=0
		num=int(input("Enter a no : "))
		print("fibonacci series :")
		for i in range(num):
			print(a)
			tmp=b
			b=a+b
			a=tmp

	elif n==9:
        # Demonstrate while-else loop
		num=6
		while num > 0:
			num=num-1
			print("I am in while loop")
		else:
			print("I am in else loop")

	elif n==10:
        # Prime numbers in given range
		num = int(input("Enter your range : "))
		flag=0
		for i in range(num):
			count = 0
			for j in range(i):
				if i%(j+1)==0:
					count=count+1
			if count==2:
				flag=flag+1
		print("Prime nos in given range : ",flag)

	elif n==11:
        # Perform string operations
		string = "governmentcollege"
		print("Second letter of word is : ",string[1:2])
		print("First four letters are : ",string[:4])
		print("Last six letters are :",string[-6::1])
	else:
        # Invalid choice
		print("wrong choice")

	print("Do you want to continue (y/n) ")
	ch=str(input())

#end of first while loop

