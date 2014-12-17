#Main program executor
import pyRecipeBook
import FoodGroups
import ShoppingList as List

#Welcome screen
welcomeMessage =  "Welcome to pyRecipeBook!\n"
welcomeMessage += "Enter a command below:\n"
print(welcomeMessage)

myShoppingList = []

#Method for `exit` command
def exitCom(args):
	#Predefined so args is never less than 1
	#Too many arguements
	if len(args) > 1:
		return True
	#Interactive mode should is not on
	return False

#Method to run commands
def runCommand(command,myShoppingList=[1]):
	#Split command
	args = command.split()
	
	#
	if len(args) < 1: #No command -> pass
		return True
	elif args[0] == 'exit': #Exit command
		print('Exiting...')
		return False
	elif args[0] == 'add': #Proceed to add what is given
		#Test whether the arguements are valid
		if len(args) == 1: #Not enough arguements
			print "Minimum of 2 arguements must be given"
		elif len(args) >4:
			print "Maximum of 4 arguements must be given"
		else: #Add item to list
			#Convert the arguements to something to input into Python method 
			newArgs = (myShoppingList,) + tuple(args[1:])
			#Add to the shopping list
			myShoppingList = addToList(*newArgs)
		return True
	else: #Command isn't defined in this tool
		print('That command doesn\'t exist.')
		return True

#Add item to shopping list
def addToList(myList,item,quantity=1,unit=''):
	myItem = List.Item(item,quantity,unit)
	myList.append(myItem)
	return myList
#
pre = '# '
on = True

#Keep asking for inpyt
while(on):
	#Enter a command
	command = raw_input(pre)
	#Run command
	on = runCommand(command)

#Exiting commands
exitMessage = "\nThank you for choosing to use pyRecipeBook!\n"	
print(exitMessage)
