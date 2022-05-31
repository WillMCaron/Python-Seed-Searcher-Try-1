
def get_seed (filename):
  myfile = open(filename, "r");
  seeds = []
  line = 1
  while (line != ""):
    line = myfile.readline()
    seeds.append(line)
  myfile.close()
  return seeds;


def dupes (filename):
  seeds = get_seed(filename);
  seeds = seeds[:len(seeds)-1]
  myfile = open(filename,"a+")
  open(filename, "w");
  lens = []
  try:
    for i in seeds:
      if i not in lens:
        lens.append(i)

  except Exception as e:
    print(e)
    for i in range(len(lens)):
      myfile.write(str(lens[i]))
    myfile.close
    
  for i in range(len(lens)):
    myfile.write(str(lens[i]))

  myfile.close();
  

def main():
  dupes("/home/runner/CalmGoodProfessionals/ones.txt");


main()
