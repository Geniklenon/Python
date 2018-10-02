summ=1
avgre= 100*12
avgrf= summ*100

def errors():
  o=str(input("do u want to cont... yes/no::  "))
  if o=="yes":
    marks()
  elif o=="no":
    print("thank u for using lolo apk!")
  else:
    print("error!!!")

def marks():
  for course in range(12):
    i=int(input("enter marks::  "))
    if i>100 or i<0 :
      print("invalid lolo marks")
      errors()
      
marks()


   
  
