a1=[1,2,3,4,5,6]
a2=[1,2,3,4,5,6]
c=0
print("The no of combinations are:")
for i in range(1,len(a1)+1):
    for j in range(1,len(a2)+1):
        c+=1
print(c)
        