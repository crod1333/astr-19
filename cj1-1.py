def PrintHelloWorld():
	print("Full name: Cristina Rodriguez")
	print("My favorite movie is Lilo & Stitch")
	print("My favorite food is Italian cuisine")

#we almost always have a 'main' function, which calls other functions 
#and performs all tasks of our program
def main():
	PrintHelloWorld()

#telling the computer that the main function, 'def main', is the first thing you start with
if __name__=='__main__':
	main()