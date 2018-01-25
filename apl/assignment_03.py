# Assignment no 3

def print_time():
	# printing time in different format
	from time import localtime
	monthList = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
	dayList = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
	t=localtime()
	format = "%s %s %d %02d:%02d:%02d IST %d"
	day=dayList[t.tm_wday]
	month=monthList[(t.tm_mon-1)]
	print format % (day,month,t.tm_mday,t.tm_hour,t.tm_min,t.tm_sec,t.tm_year)

def file_upper(filename):
	# printing file content in upper case
	infile = open(filename)
	lines=infile.readlines()
	infile.close()
	for line in lines:
		print line.upper()

def file_sort(filename):
	# alphabetically sorts file
	infile = open(filename)
	lines=infile.readlines()
	infile.close()
	lines.sort()
	outfile = open(filename,'w')
	outfile.writelines(lines)
	outfile.close()
	print("File sorted.")

char="Y"
while (char is "Y" or char is "y"):
    # program menu
	print("Program menu")
	print("1.File uppercase ")
	print("2.Functions with default arguments")
	print("3.Print Time")

	print("\nEnter yout choice : ")
	n=int(input())

	if n==1:
		# File in uppercase 
		print("Enter full filename ")
		filename = raw_input()
		file_upper(filename)
	elif n==2:
		# File in sorted order
		print("Enter full filename ")
		filename = raw_input()
		file_sort(filename)
	elif n==3:
		# Print date
		print_time()
	else:
		# Invalid choice
		print("wrong choice")

	print("Do you want to continue (y/n) ")
	char=raw_input()
#end of first while loop
