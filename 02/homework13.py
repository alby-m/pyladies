number_of_legs = float(input("How many legs do you have? "))

while number_of_legs == (number_of_legs*10)%10>0:
    print("We count only whole legs, sorry.")
    
    number_of_legs = float(input("How many legs do you have? "))

    if  (number_of_legs*10)%10>0:
        print("We count only whole legs, sorry.")
        #decimal number
    elif number_of_legs%2 == 1  and number_of_legs != 1:
        print("You are not local, right?")
        #odd number
    elif number_of_legs>10:
        print("How much money do you spend for shoes, Mr Centipede?")
        #centipede
    elif number_of_legs>8:
        print("Probably not fan of crab sticks...")
        #crab
    elif number_of_legs>6:
        print("Those webs, sir, really piece of artwork!")
        #spider
    elif number_of_legs>4:
        print("Got some honey for sale?")
        #bee
    elif number_of_legs>2:
        print("Catched a ball? Good boy!")
        #dog
    elif number_of_legs>1:
        print("You think you are the top of the evolution. Interesting...")
        #human
    elif number_of_legs>0:
        print("I think it's pretty awesome to carry your house with you all the time.")
        #snail`
    elif number_of_legs == 0:
        print("Lying while moving, that's the dream!") 
        #snake
    else:
        print('Did you have too much to drink?')