
z = 1.5 + 1.5

def numbers():
	print(z)
	print(type(z))
	print(7 - 9)
	print(type(7-9))
	print(2.5 * 10)
	print(type(2.5 * 10))

# we almost always have a 'main' function, which calls other functions 
# and performs all tasks of our program
def main():
	numbers()

#telling the computer that the main function, 'def main', is the first thing you start with
if __name__=='__main__':
	main()