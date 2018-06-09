import random

for x in range(6):
    roll_input = raw_input("Select your action: Roll = R or quit = Q\n")
    if roll_input.lower() ==  "r": 
      rand = random.randint(1,6)
      print "You rolled a " + str(rand)
    elif roll_input.lower() == "q":
     print("You did not roll")
     quit()


