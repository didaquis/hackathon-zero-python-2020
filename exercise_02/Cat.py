class Cat: 
	"Class for create cats object"

	def __init__(self, name):
		self.name = name
	
	def getName(self):
		return self.name

	def talk(self):
		return 'miau'