# For XML Element Tree manipulation
import xml.etree.ElementTree as ET #place within somewhere?


# FoodGroups object inspired by P90X
class FoodGroups:
    # Other Properties shared for all objects (constant)
    groups = ['Fats','Carbs','Dairy','Fruit','Snacks','Proteins',
              'Condiments','Vegetables']

    # Snack object
    class Snack:
        # String representation of object
        def __repr__(self):
            return ET.tostring(self.xml)
        # Converting to string
        def __str__(self):
            return ET.tostring(self.xml)    
        # Initiate Snack object with number of servings (default to 0)
        def __init__(self,SGL=0,DBL=0,BAR=0,DRINK=0):
            self.SGL   = SGL
            self.DBL   = DBL
            self.BAR   = BAR
            self.DRINK = DRINK
            self.xml = self.__createXML() #XML representation of object
        
        # Create XML instance of the object
        def __createXML(self):
            snack = ET.Element('snack') #create root element
            # Create subelements  
            sgl   = ET.SubElement(snack,'sgl')
            dbl   = ET.SubElement(snack,'dbl')
            bar   = ET.SubElement(snack,'bar')
            drink = ET.SubElement(snack,'drink')
            # Text within tag
            sgl.text='%0.1f' %self.SGL
            dbl.text='%0.1f' %self.DBL
            bar.text='%0.1f' %self.BAR
            drink.text='%0.1f' %self.DRINK
            # Give XML instance
            return snack

    # String representation of object
    def __repr__(self):
        return ET.tostring(self.xml)
    # Converting to string
    def __str__(self):
        return ET.tostring(self.xml)     
    # Initiate object with number (decimal or int)
    def __init__(self,fats=0,carbs=0,proteins=0,dairy=0,fruit=0,vegetables=0,
                condiments=0,snacks=Snack()):
        self.fats       = fats
        self.carbs      = carbs 
        self.dairy      = dairy
        self.fruit      = fruit
        self.snacks     = snacks     #object with four types (SGL,DBL,BAR,DRINK)
        self.proteins   = proteins
        self.condiments = condiments
        self.vegetables = vegetables
        self.xml        = self.__createXML() #XML representation of object

    # Create XML instance of the object
    def __createXML(self):
        foodGroups = ET.Element('foodGroups') #create root element
        # Create subelements
        fats       = ET.SubElement(foodGroups,'fats')
        carbs      = ET.SubElement(foodGroups,'carbs')
        dairy      = ET.SubElement(foodGroups,'dairy')
        fruit      = ET.SubElement(foodGroups,'fruit')
        snacks     = foodGroups.append(self.snacks.xml) #XML from Snack instance
        proteins   = ET.SubElement(foodGroups,'proteins')
        condiments = ET.SubElement(foodGroups,'condiments')
        vegetables = ET.SubElement(foodGroups,'vegetables')
        # Text within tag 
        fats.text       = '%0.1f' %self.fats
        carbs.text      = '%0.1f' %self.carbs
        dairy.text      = '%0.1f' %self.dairy
        fruit.text      = '%0.1f' %self.fruit
        proteins.text   = '%0.1f' %self.proteins
        condiments.text = '%0.1f' %self.condiments 
        vegetables.text = '%0.1f' %self.vegetables
        # Give XML instance
        return foodGroups

    # Define functions to change properties (thus XML)
    # Must use Snacks class properly to change values
    # USe the @property aspects


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

