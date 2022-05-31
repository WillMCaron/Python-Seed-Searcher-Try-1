from random import randint,seed, random
from time import time
from math import floor, ceil

def lucas(goal):
  seedeth = ceil(time()*random());
  seed(seedeth);
  count = 1;
  num = randint(0,100000);
  if (num != goal):
    count += 1
  return count, seedeth


def save(seed, filename):
  with open(filename, "a") as f:
    f.write(str(seed) +"\n")
    f.close()

def will (goal) :
  t_start = time();
  count, seedeth = lucas(goal)
  lapses = 1;
  while (count > 1):
    lapses +=1 
    count,seedeth = lucas(goal);
  elapsed = time()-t_start;

  print("Time Elapsed:",elapsed)
  print("I searched", lapses,"seeds!")
  print("The seed was",seedeth)
  print("It found",goal,"in",count, "tries!")
  print()
  save(seedeth, 
  "/home/runner/CalmGoodProfessionals/ones.txt");
  #secs = floor();
  #save(secs, "/home/runner/ShockedSeveralCoins/texts/times.txt");


def main():
  for i in range(500):
    will(72727)
  
main()
