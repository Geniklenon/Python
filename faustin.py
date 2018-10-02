t="level"
def dinning():
  print("Welcome to Dinning service room")
  print("Service allowance requires fact of 4 levels with 5 needs")
  for i in range(5):  
    x=int(input("which level are u on? :::  "))
    if x==1:
      print("take food \n\n")
    elif x<i:
      print("out of the members of level \n\n")
    else:
      print("keep rising on next ",x-1,t)
for s in range(10000000000000000):
  dinning()
