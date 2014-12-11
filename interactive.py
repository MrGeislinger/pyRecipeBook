#Main program executor
import pyRecipeBook
import FoodGroups

#Welcome screen
welcomeMessage =  "Welcome to pyRecipeBook!\n"
welcomeMessage += "Enter a command below:\n"
print(welcomeMessage)

#Method to run commands
def runCommand(command):
	if command.strip() == 'exit':
		return False
	else:
		return True

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