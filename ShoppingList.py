#Shopping list

#Item
class Item:
	#Initiate with an item, defaults to 1 quantity of no special unit
	def __init__(self,name,quantity=1,unit=''):
		self.name = name
		self.quantity = quantity
		self.unit = unit

	#Getters
	def getName():
		return self.name
	def getQuantity():
		return self.quantity
	def getUnit():
		return self.unit
	def getItem():
		return (self.name, self.quantity, self.unit)

