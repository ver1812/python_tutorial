def pretty(f):
	def inner():
		print("*"*50)
		f()
		print("*"*50)
	return inner


@pretty
def welcome():
	print("Good Evening")


@pretty
def bye():
	print("Good bye")


welcome()
bye()