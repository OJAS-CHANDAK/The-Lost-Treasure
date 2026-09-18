print("Dead Man's Coordinates")
print("An ancient chest is buried between the grid of 100*100 sq.km")
\n
\n
import random
import math
treasure_location_x = random.randint(1,100)
treasure_location_y = random.randint(1,100)
guess_x = 0
guess_y = 0
while guess_x!=treasure_location_x&&guess_y!=treasure_location_y:
  d = (x-a)*(x-a)+(y-b)*(y-b)
  d = math.sqrt(d)
  print(d)
print("You found the location of the trasure")



