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

