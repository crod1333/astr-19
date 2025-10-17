import numpy as np
from astropy.table import Table
from astropy.io import ascii

#main program
def main():

	x = np.linspace(0,2.0*np.pi,1000) #creates 1000 floating numbers 
									# from 0 to 2pi
	data = Table([np.sin(x),x],names=['sin(x)','x']) # create table

	ascii.write(data, 'table#5.txt', format='commented_header') #write 
													#table to the file
	data_in = ascii.read('table#5.txt') # read in data

	print(data_in) #print data

#run the program
if __name__ == "__main__":
	main()