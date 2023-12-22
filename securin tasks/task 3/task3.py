a1=[1,2,3,4,5,6]
a2=[1,2,3,4,5,6]
x=0
c=0
for i in range(1,len(a1)+1):
    for j in range(1,len(a2)+1):
        x+=1
for i in range(1,len(a1)+1):
    for j in range(1,len(a2)+1):
        if(i+j==3):
           c+=1
print("the probality is :",c,"/",x,)
