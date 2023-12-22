a1=[1,2,3,4,5,6]
a2=[1,2,3,4,5,6]
matrix=[]
for i in range(1,len(a1)+1):
    r=[]
    for j in range(1,len(a2)+1):
        r.append((i,j))
    matrix.append(r)
for i in matrix:
    print(i)

     

