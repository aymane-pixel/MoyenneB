#Version1
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


#Moyenne Liste - V2
matieres = []
coefficients_UE1 = [10, 10, 7, 7, 0, 5, 0, 6, 0, 5, 4, 2, 5, 5, 0, 20, 20, 0, 0, 0, 7]
coefficients_UE2 = [4, 0, 2, 8, 6, 0, 0, 0, 0, 5, 5, 2, 9, 9, 3, 0, 0, 29, 0, 0, 7]
coefficients_UE3 = [4, 0, 2, 0, 0, 5, 15, 6, 4, 5, 5, 2, 0, 0, 3, 0, 0, 0, 20, 20, 7]

notes_etudiant = []

for i in range(101,116):
    matieres.append("R{}".format(i))
for i in range(11,17):
    matieres.append("SAE{}".format(i))

for i in range(101,116):
    notes_etudiant.append(float(input("Notes de R{}".format(i))))
for i in range(11,17):
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
    print("Moyenne de {} : {}".format(nom_ue, round(moyenne,3)))
    
calculer_moyenne_ue("UE1", coefficients_UE1, notes_etudiant)
calculer_moyenne_ue("UE2", coefficients_UE2, notes_etudiant)
calculer_moyenne_ue("UE3", coefficients_UE3, notes_etudiant)

#Version 3 / dico
matiere = []
liste_notes = [i for i in range(21)]
coefficients_UE1 = [10, 10, 7, 7, 0, 5, 0, 6, 0, 5, 4, 2, 5, 5, 0, 20, 20, 0, 0, 0, 7]
coefficients_UE2 = [4, 0, 2, 8, 6, 0, 0, 0, 0, 5, 5, 2, 9, 9, 3, 0, 0, 29, 0, 0, 7]
coefficients_UE3 = [4, 0, 2, 0, 0, 5, 15, 6, 4, 5, 5, 2, 0, 0, 3, 0, 0, 0, 20, 20, 7]
for i in range(101,116):
    matiere.append("R{}".format(i))
for i in range(11,17):
    matiere.append("SAE{}".format(i))
def dico(liste_valeurs):
    return {cle : valeur for cle, valeur in zip(matiere,liste_valeurs)}

dico_notes = dico(liste_notes)
dico_coef1 = dico(coefficients_UE1)
dico_coef2 = dico(coefficients_UE2)
dico_coef3 = dico(coefficients_UE3)

def moyenne_UE1():
    somme = 0
    total_coef1 = 0
    for element in matiere:
        somme += dico_coef1[element]*dico_notes[element]
        total_coef1+= dico_coef1[element]
    moy1 = round((somme/total_coef1),3)
    print(f"La moyenne de l'UE1 est", moy1)
moyenne_UE1()

def moyenne_UE2():
    somme = 0
    total_coef2 = 0
    for element in matiere:
        somme += dico_coef2[element]*dico_notes[element]
        total_coef2+= dico_coef2[element]
    moy2 = round((somme/total_coef2),3)
    print(f"La moyenne de l'UE2 est", moy2)
moyenne_UE2()

def moyenne_UE3():
    somme = 0
    total_coef3 = 0
    for element in matiere:
        somme += dico_coef3[element]*dico_notes[element]
        total_coef3+= dico_coef3[element]
    moy3 = round((somme/total_coef3),3)
    print(f"La moyenne de l'UE3 est", moy3)
moyenne_UE3()



