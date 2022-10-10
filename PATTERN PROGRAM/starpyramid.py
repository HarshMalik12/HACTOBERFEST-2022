#To print left aligned star pyramid,right algined star pyramid and center aligned using for and while loop

def leftpyr(s):
    for i in range(1,s+1):
        print('*'*i)

def rightpyr(s):
    for i in range(1,s+1):
        print(' '*(s-i)+'*'*i)

def centerpyr(s):
    k=s
    for i in range(1,s+1):
        print(" "*(k-1)+"* "*i)
        k=k-1
while(True):
    type=int(input("Enter the number for the type of pyramid\n1.Left Aligned\n2.Right Aligned\n3.Center Aligned\n0 to exit\n : "))
    if(type==0):
        break
    s=int(input("Enter the size of the pyramid: "))
    if(type==1):
        leftpyr(s)
    elif(type==2):
        rightpyr(s)
    elif(type==3):
        centerpyr(s)

    else:
        print("Invalid number")

