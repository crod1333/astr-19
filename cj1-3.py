'''Write a Python program that defines a function f(x) that returns x**3 + 8. 
In the main function of the program, call f(x) with x = 9 and print the result.  
Use an if statement that executes if the result is larger than 27 and prints “YAY!”.
'''

#experimenting with user input
import sys

def math_expression(x):
	if x**3 + 8 > 27:
		# giving a more detailed description to the user of what's happening.
		print(f"The answer to \'x^3 + 8\' equals {x**3 + 8}")
		print("YAY!")
	else:
		# if the answer is less than 27, only the answer will print.
		print(f"The answer to \'x^3 + 8\' equals {x**3 + 8}")

# main program
def main():

# want users to input a number for x, grabbing it from the console
	if (len(sys.argv)<=2):
		# Using "try" and "except" so that user doesn't get an error if they
		# don't input a second argument (the number) in the console. Instead, it simply tells
		# them to input a number. Makes the program cleaner.
		try:
			#set x equal to the 2nd input in the console
			x = int(sys.argv[1])
			# telling the user what they input
			print(f"You entered: {x}" + " for x.")
			# running the math equation for the number they input
			math_expression(x)
		except:
			#incase the user doesn't enter a number
			print("Enter a number after the file name.")

# run the program
if __name__=='__main__':
	main()