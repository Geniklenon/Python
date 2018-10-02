import time
localtime=time.localtime(time.time())
print("The curent local time is: ",localtime)

def Today():
      localtime=time.asctime(time.localtime(time.time()))
      print(localtime)
