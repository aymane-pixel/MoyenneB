#!/usr/bin/env python
# coding: utf-8

# In[25]:


#VERSION_5
import matplotlib.pyplot as plt
from PIL import Image as PILImage, ImageTk 
from tkinter import*
from tkinter import ttk
import numpy as np
fen = Tk()
fen.geometry("1100x800")
frm = ttk.Frame(fen)
frm.grid()
coef1 = [10, 10, 7, 7, 0, 5, 0, 6, 0, 5, 4, 2, 5, 5, 0, 20, 20, 0, 0, 0, 7]
coef2 = [4, 0, 2, 8, 6, 0, 0, 0, 0, 5, 5, 2, 9, 9, 3, 0, 0, 29, 0, 0, 7]
coef3 = [4, 0, 2, 0, 0, 5, 15, 6, 4, 5, 5, 2, 0, 0, 3, 0, 0, 0, 20, 20, 7]
matieres = []
saisies = []
for i in range(101,116):
    matieres.append("R{}".format(i))
for i in range(11,17):
    matieres.append("SAE{}".format(i))
for i in range(len(matieres)):
    objet1 = ttk.Label(frm, text=matieres[i])
    objet1.grid(column=0, row=i, padx=10, pady=5)

    objet2 = ttk.Entry(frm)
    objet2.grid(column = 1,row = i)
    saisies.append(objet2)

canvas = Canvas(frm, width=450, height=350, bg='white')
canvas.grid(column=4, row=1, rowspan=15, padx=20)

def recup():
    global img
    notes = [float(data.get()) for data in saisies]

    val_moy1 = round(np.average(notes, weights=coef1), 3)
    val_moy2 = round(np.average(notes, weights=coef2), 3)
    val_moy3 = round(np.average(notes, weights=coef3), 3)

    UE1 = ttk.Label(frm, text="Moyenne de l'UE1")
    UE1.grid(column=2, row=3, pady=20)
    moy1 = ttk.Label(frm, text=val_moy1, relief=GROOVE)
    moy1.grid(column=3, row=3, pady=20)

    UE2 = ttk.Label(frm, text="Moyenne de l'UE2")
    UE2.grid(column=2, row=4, pady=20)
    moy2 = ttk.Label(frm, text=val_moy2, relief=GROOVE)
    moy2.grid(column=3, row=4, pady=20)

    UE3 = ttk.Label(frm, text="Moyenne de l'UE3")
    UE3.grid(column=2, row=5, pady=20)
    moy3 = ttk.Label(frm, text=val_moy3, relief=GROOVE)
    moy3.grid(column=3, row=5, pady=20)

    with plt.style.context('Solarize_Light2'):
        ues = ["UE 1", "UE 2", "UE 3"]
        moyennes = [val_moy1, val_moy2, val_moy3]
        plt.clf()  
        couleurs = ["red" if m < 8 else "orange" if m <= 10 else "green" for m in moyennes]
        plt.bar(ues, moyennes, color=couleurs)
        plt.title("Moyenne UE1 / UE2 / UE3")
        plt.xlabel("Unités d'Enseignement")
        plt.ylabel("Moyennes / 20")
        plt.ylim(0, 20) 
        plt.grid(axis='y', linestyle='--')
        plt.tight_layout() 
        plt.savefig("mon_graphique.png")
        plt.close()
        image_originale = PILImage.open("mon_graphique.png")
        image_redimensionnee = image_originale.resize((450, 350))
        img = ImageTk.PhotoImage(image_redimensionnee)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=NW, image=img)



btn = ttk.Button(frm,text = "Valider", command = recup)
btn.grid(column = 2, row = 1,padx = 30)

fen.mainloop()

