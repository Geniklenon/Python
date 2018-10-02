def CALC():
  print("Welcome to Geniklenon CALCULATOR")
  x=int(input("enter first number: "))
  sign=str(input("Operator SIGN::  "))
  y=int(input("enter second number: "))
  add=x+y
  sub=x-y
  div=x/y
  prod=x*y

  if (sign=="+"):
    print("Addition of ",x,"+",y,"=",add)
  elif (sign=="-"):
    print(sub)
  elif (sign=="/"):
    print(div)
  elif (sign=="X"):
    print(prod)
  else:
    print("invalid input")

  print("Thanks for using Geniklenon Calculator")

for x in range(1,10000000000000000000000000000000000000000000000000000):
  CALC()

