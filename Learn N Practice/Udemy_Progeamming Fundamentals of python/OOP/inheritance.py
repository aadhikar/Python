class Parent():
	"""
	This is Parent class.
	"""
	def __init__(self, last_name, eye_color):
		print "{0}".format("Parent constructor called");
		self.last_name = last_name;
		self.eye_color = eye_color;

	def show_info(self):
		print "Last name is {0}".format(self.last_name);
		print "Eye color is {0}".format(self.eye_color);
		
class Child(Parent):
	"""
	This is Child class and inherits properties from Parent class.
	"""
	def __init__(self, last_name, eye_color, number_of_toys):
		print "{0}".format("Child constructor called");
		Parent.__init__(self, last_name, eye_color);
		self.number_of_toys = number_of_toys;
	
	# This method will override show_info inherited from Parent class.
	def show_info(self):
		print "Last name is {0}".format(self.last_name);
		print "Eye color is {0}".format(self.eye_color);
		print "Have {0} toys".format(str(self.number_of_toys));


tom_cruise = Parent("Cruse", "Blue");
# print "{0}".format(tom_cruise.last_name);
# tom_cruise.show_info();

mikey_mouse = Child("Mouse", "Green", 5);
# print "My last name is {0} and I have {1} toys.".format(mikey_mouse.last_name, mikey_mouse.number_of_toys);
mikey_mouse.show_info();