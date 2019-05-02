class Observance:
    def __init__(self, NAME, DESCRIPTION):
        self.name = NAME
        self.description = DESCRIPTION
        #self.is_item = IS_ITEM
        
    def describe(self):
        print('\n' + self.name + "--- " + self.description + '\n')  
