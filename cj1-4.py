
# Write a Python program that declares a class describing your favorite animal. 
# Have the data members of the class represent the following physical parameters 
# of the animal: length of the arms (float), length of the legs (float), number 
# of eyes (int), does it have a tail? (bool), is it furry? (bool). Write an 
# initialization function that sets the values of the data members when an instance 
# of the class is created. Write a member function of the class to print out and 
# describe the data members representing the physical characteristics of the animal.

class Animal:
	# introduce parameters (data members)
	def __init__(self, name, len_arms, len_legs, num_eyes, has_tail, has_fur):
		# setting values of parameters
		# "self" is calling back to the class. Has to be 1st parameter
		self.name = name
		self.len_arms = len_arms
		self.len_legs = len_legs
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.has_fur = has_fur

	#printing out the objects characteristics
	def	describe(self):
		print(f"Animal name: {self.name}")
		print(f"Length of arms: {self.len_arms}")
		print(f"Length of legs: {self.len_legs}")
		print(f"Number of eyes: {self.num_eyes}")
		print(f"Has a tail: {self.has_tail}")
		print(f"Is furry: {self.has_fur}")

#main program
def main():
	# defining a class variable "cat"
	cat = Animal("Cat", 12.5, 13.0, 2, True, True)
	# calling the "describe" function, which prints 
	# the details of the animal
	cat.describe()

#run the program
if __name__ == "__main__":
	main()