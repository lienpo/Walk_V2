#from location import Location
from player import Player

You = Player("Streets")

out = False

while( not out ):
        option = input("What to you want to do? --talk(1)  --leave(2) --look around(3) (Enter 0 to quit)? ")
        if( option == 1 or option == 2 or option == 3):
                You.verify_selection(option)
                
        elif( option == 0 ):
                out = True
        else:
                print("That is not a valid option")

