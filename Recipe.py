# Recipe object
class Recipe:
    # Initiate object
    def __init__(self,name,info,ingredients=[],steps=[]):
        self.name        = name    #name of recipe
        self.info        = info    #other recipe info (calories,servings,etc.?)
        self.steps       = steps   #list of steps
        self.ingredients = ingredients #array of Ingredient objects

    # Change name of recipe
    def changeName(name):
        self.name = name

    # Change info about recipe
    def changeInfo(info):
        self.info = info

    # Add Ingredient object to the recipe
    def addIngredient(ingredient):
        self.ingredients.append(ingredient)

    # Add next step to the recipe
    def addStep(step):
        self.steps.append(step)

    # Move step up
    def moveStepUp(stepIndex):
        # Check that index can be moved up by one (not first & within array)
        if (stepIndex > 0) and (stepIndex < len(self.steps)):
            # Insert 1 position up after popping step off list
            self.steps.insert(stepIndex-1, self.steps.pop(stepIndex))

    # Move step down
    def moveStepUp(stepIndex):
        # Check that index can be moved down by one (within array & not last)
        if (stepIndex>=0) and (stepIndex < len(self.steps) - 1):
            # Insert 1 position down after popping step off list
            self.steps.insert(stepIndex+1, self.steps.pop(stepIndex))

    def moveStepTo(stepIndex,newIndex):
        # Check that stepIndex is within array
        if (stepIndex>=0) and (stepIndex<len(self.steps)):
            # Check that newIndex is within array
            if (newIndex>=0) and (newIndex<len(self.steps)):
                self.steps.insert(newIndex,self.steps.pop(stepIndex))
