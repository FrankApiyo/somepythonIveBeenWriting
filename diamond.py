class BaseClass:
	"""super keyword was originally ment for dealing with complicated
	forms of multiple inheritance. this calls the next method in the 
	hirarchy which may not neccesarily be the parent method """
	num_base_calls = 0
	def call_me(self):
		print("calling method on Base class")
		self.num_base_calls += 1

class LeftSubclass(BaseClass):
	num_left_calls = 0
	def call_me(self):
		super().call_me()
		print("calling method on Left Subclass")
		self.num_left_calls += 1

class RightSubclass(BaseClass):
	num_right_calls = 0
	def call_me(self):
		super().call_me()
		print("calling method on right subclass")
		self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
	num_sub_calls = 0
	def call_me(self):
		super().call_me()
		print("calling method on subclass")
		self.num_sub_calls += 1