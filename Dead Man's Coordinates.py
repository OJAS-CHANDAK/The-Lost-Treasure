print("Dead Man's Coordinates")
print("An ancient chest is buried between kilometers 1 and 100.")
print()
print()
import random
treasure_location = random.randint(1,100)
guess = 0
while guess!=treasure_location:
    try:
        guess = int(input("Enter Target Coordinate: "))
        if(guess<treasure_location):
            diff = treasure_location - guess
            print("The Treasure is Further Ahead!")
            print()
        elif(guess>treasure_location):
            diff = guess - treasure_location
            print("You Passed It! Turn Back.")
            print()
        else:
	        print("You Found The Treasure")
    except ValueError:
    
        print("Please Enter A Valid Number.")
        print()