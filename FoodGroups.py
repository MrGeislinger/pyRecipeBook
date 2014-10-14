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
