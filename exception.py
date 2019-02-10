import random
some_exception = [ValueError, TypeError, IndexError, None]

try:
	choice = random.choice(some_exception)	
	print("raising {}".format(choice))
	if choice:
		raise choice("An error")
except ValueError:
	print("Caught a ValueError")
except TypeError:
	print("Caught a TypeError")
except Exception as e:
	print("Caught some other error: %s" % 
		(e.__class__.__name__))
else:
	print("this code called if there is no exception")
finally:
	print("this cleanump code is always called")