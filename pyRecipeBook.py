
# Recipe Info object (inherit from `P90XInfo` class)
class RecipeInfo:   

    # P90X properties default to `None`
    # self.p90X

    # Initiate RecipeInfo object
    def __init__(self,calories=0,servingSize='',servings=1,difficulty=None,notes=''):
        self.notes       = notes       #notes about recipe
        self.servings    = servings    #number of servings recipe yields
        self.calories    = calories    #calories per serving
        self.difficulty  = difficulty  #
        self.servingSize = servingSize #size of one serving

        # Other Properties 
        # Default to `None` (no information; all in grams)
        self.fat        = None
        self.carb       = None
        self.fiber      = None
        self.sodium     = None
        self.protein    = None
        self.cholestrol = None

    # Set nutrition amount per serving in grams
    def setNutrition(fat=None,carb=None,fiber=None,sodium=None,protein=None,cholestrol=None):
        # Only set the nutrition if user gave a value
        if fat!=None:
            self.fat        = fat
        if carb!=None:
            self.carb       = carb
        if fiber!=None:
            self.fiber      = fiber
        if sodium!=None:
            self.sodium     = sodium
        if protein!=None:
            self.protein    = protein
        if cholestrol!=None:
            self.cholestrol = cholestrol

    # Set/Change note section
    def setNote(note):
        self.notes = note

    # Set/Change calories
    def setCalories(cal):
        self.calories = cal

    # Set/Change serving size
    def setServingSize(servingSize):
        self.servingSize =servingSize


# Step object
class Step:
    # Initiate object
    def __init__(self,description):
        self.description = description

# Ingredient object
class Ingredient:
    # Initiate object
    def __init__(self,name,amount,measurement="",prepared=""):
        self.name        = name        #ingredient
        self.amount      = amount      #amount of ingredient (no scale)
        self.prepared    = prepared    #how was ingredient prepared
        self.measurement = measurement #how ingredient is measured
        
    # Set name of ingredient 
    def setName(name):
        self.name = name

    # Set amount of ingredient (and change measurement type if given)
    def setAmount(amount,measurement=None):
        self.amount      = amount
        # Don't set measurement type if not given by user
        if measurement!=None:
            self.measurement = measurement 

    # Set how amount is measured
    def setMeasurement(measurement):
        self.measurement = measurement

    # Set how prepared
    def setPrepared(prepared):
        self.prepared = prepared


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

