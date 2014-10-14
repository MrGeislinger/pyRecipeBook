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
