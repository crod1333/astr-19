import numpy as np

def main():
	i = 0 #integers can be declared with a number
	n = 10 #here is another integer
	x = 19.0 #floating point numbers are declared with a ".""

	#we can use numpy yo declare arrays quickly

	y=np.zeros(n,dtype=float) #declares 10 zeros as floats using np

	#we can use for loops to iterate with a varibale

	for i in range(n):
		y[i] = 2.0 * float(i) + 1.	#set y = 2i+1 as floats

		#we an also simply iterate throug a variable
	for y_element in y:
		print(y_element)

#execute 'main' function
if __name__=="__main__":
	main()



