#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Moyenne_UE1():
    som_1 = 0
    coe_1 = 0
    moy_1 = 0
    for i in range(101,104):
        note=float(input("Note de R{}".format(i)))
        coeff=int(input("Coeff de R {}".format(i)))
        som_1+=note*coeff
        coe_1+=coeff
    for i in range(11,13):
        note = float(input("Note de SAE{}".format(i)))
        coeff = int(input("Coeff de SAE{}".format(i)))
        som_1+= note*coeff
        coe_1 += coeff
    moy_1 = som_1 / coe_1
    print("Moyenne de UE1 : ",round(moy_1,2))
Moyenne_UE1()
def Moyenne_UE2():
    som_1 = 0
    coe_1 = 0
    moy_1 = 0
    for i in range(101,104):
        note=float(input("Note de R{}".format(i)))
        coeff=int(input("Coeff de R {}".format(i)))
        som_1+=note*coeff
        coe_1+=coeff
    for i in range(11,13):
        note = float(input("Note de SAE{}".format(i)))
        coeff = int(input("Coeff de SAE{}".format(i)))
        som_1+= note*coeff
        coe_1 += coeff
    moy_1 = som_1 / coe_1
    print("Moyenne de UE2 : ",round(moy_1,2))
Moyenne_UE2()
def Moyenne_UE3():
    som_1 = 0
    coe_1 = 0
    moy_1 = 0
    for i in range(101,104):
        note=float(input("Note de R{}".format(i)))
        coeff=int(input("Coeff de R {}".format(i)))
        som_1+=note*coeff
        coe_1+=coeff
    for i in range(11,13):
        note = float(input("Note de SAE{}".format(i)))
        coeff = int(input("Coeff de SAE{}".format(i)))
        som_1+= note*coeff
        coe_1 += coeff
    moy_1 = som_1 / coe_1
    print("Moyenne de UE3 : ",round(moy_1,2))
Moyenne_UE3()    


# In[ ]:




