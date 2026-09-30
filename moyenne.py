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
#Moyenne Liste
matieres = ["R101", "R102", "R103", "SAE11", "SAE12"]
coefficients_UE1 = [10, 10, 7, 20, 20]
coefficients_UE2 = [4, 0, 2, 0, 0]
coefficients_UE3 = [4, 0, 2, 0, 0]
notes_etudiant = []

for i in range(101,104):
    notes_etudiant.append(float(input("Notes de R{}".format(i))))
for i in range(11,13):
    notes_etudiant.append(float(input("Notes de SAE{}".format(i))))

def calculer_moyenne_ue(nom_ue, coefficients, notes):
    somme_points = 0
    somme_coefficients = 0
    for i in range(len(notes)):
        coeff = coefficients[i]
        if coeff > 0:
            somme_points += notes[i] * coeff
            somme_coefficients += coeff
    moyenne = somme_points / somme_coefficients
    print("Moyenne de {} : {}".format(nom_ue, round(moyenne,2)))
    
calculer_moyenne_ue("UE1", coefficients_UE1, notes_etudiant)
calculer_moyenne_ue("UE2", coefficients_UE2, notes_etudiant)
calculer_moyenne_ue("UE3", coefficients_UE3, notes_etudiant)



