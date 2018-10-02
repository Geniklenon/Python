print("WELCOME TO THE DICTIONARY SAMPLE")
def Genik():
    dict = {'Geniklenon':'He is lovely boy','God':'Almight everything creator','Ntat':'She is a girl who has taken Geniklenon full heart','Diane':'She is patient Girl'}
    word=str(input("Enter the word to find: "))
    if (word=="Geniklenon"):
        print (dict['Geniklenon'])
    elif (word=="God"):
        print(dict['God'])
    elif (word=="Ntat"):
        print(dict['Ntat'])
    elif (word=="Diane"):
        print(dict["Diane"])
    else:
        print("Not Available sorry!!!!")
    Tick = time.time()
    print(Tick)
e=1
for e in range (1,1000000000000000000000000000000000000000000000000000000000000):
    Genik()
        
    
    

    
    



