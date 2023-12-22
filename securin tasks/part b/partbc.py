def undoom_dice(a1,a2):
    i_p=calp(a1,a2)
    New_dice_A=[0]*6
    New_dice_B=a2.copy()
    l_s=6
    j=0
    h=0
    comb=[]
    def gen_comb(c_c, d):
        p_va=[1,2,3,4]
        if d==l_s:
            comb.append(list(c_c))
            return
        for v in p_va:
            c_c[d]=v
            gen_comb(c_c,d+1)

    gen_comb([0]*l_s,0)

    for i in range(len(a2)):
        New_dice_B[i]+=h
        for j in range(len(comb)):
            New_dice_A=comb[j]
        f_p=calp(New_dice_A,New_dice_B)
        if i_p==f_p:
            return New_dice_A,New_dice_B

    return None,None
def calp(a1, a2):
    sum_val=0
    d={}
    for i in range(len(a1)):
        for j in range(len(a2)):
            sum_val=a1[i]+a2[j]
            d[sum_val]=d.get(sum_val,0)+1
    for k in d:
        d[k]=d[k]/(6**2)
    return d

a1=[1,2,3,4,5,6]
a2=[1,2,3,4,5,6]
New_Die_A,New_Die_B=undoom_dice(a1,a2)
print(New_Die_A)
print(New_Die_B)
