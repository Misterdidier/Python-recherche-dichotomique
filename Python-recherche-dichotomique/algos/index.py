'''
TABLEAU DES VOYELLES
'''
import array
import time

start = time.time() * 1000

print(start)
tab_voyelles = array.array('u')
voyelles = ["a", "e", "i", "o", "u"]
i = y = 0

while i < len(voyelles):
    if y < 1000000:
        y += 1
        continue

    tab_voyelles.append(voyelles[i])
    i += 1


print(tab_voyelles)
stop = time.time() * 1000
print(stop)

print(stop - start)

'''
LES TABLEAUX
'''
# import array as ar
# import math
#
# nombres = ar.array('i', range(0, 4))
#
# for i in nombres:
#     nombres[i] = int(math.pow(i, 2))
#     print(i, "=", nombres[i], end="\t")

'''
TABLEAU DE VALEURS NEGATIVES ET/OU POSITIVES
'''
# import array as ar
#
# nbre_valeurs = int(input("Combien de valeur entrerez-vous? "))
# tab_valeurs = ar.array('i')
# i = 0
# val_negatives = val_positives = 0
#
# while i < nbre_valeurs:
#     a = int(input("Entrez la valeur {} : ".format(i)))
#     if a < 0:
#         val_negatives += 1
#     else:
#         val_positives += 1
#     tab_valeurs.append(a)
#     i += 1
#
# print("Valeurs negatives = ", val_negatives,
#       "\n Valeurs positives = ", val_positives)


'''
TABLEAU + TABLEAU = TABLEAU
'''
# import array as arr
#
# print("\t ADDITION DE DEUX TABLEAUX.................")
#
# nbres1 = arr.array('i')
# nbres2 = arr.array('i')
# tab_som = 0
#
# nb_valeurs = int(input("Quelle taille feront vos tableaux?"))
#
# for i in range(0, nb_valeurs):
#     a = int(input("Entrez le nombre {} (tableau 1)".format(i)))
#     b = int(input("Entrez le nombre {} (tableau 2)".format(i)))
#
#     tab_som = a + b
#
#     nbres1.append(a)
#     nbres2.append(b)
#
#     print("tableau 3 : indice ", i, "; VALEUR = ", tab_som)


'''
SCHTROUMPF DE TABLEAUX
'''
# import array
#
# tab_1 = array.array('i', [4, 8, 7, 12])
# tab_2 = array.array('i', [3 ,6])
# schtroumpf = 0
#
# for i in tab_2:
#     for j in tab_1:
#         schtroumpf += i*j
#
# print(schtroumpf)

'''
MAX DANS UN TABLEAU SAISI
'''
# import array
#
# print("AFFICHAGE DE LA VALEUR MAX DANS UN TABLEAU SAISI PAR VOUS!!!")
#
# tab_valeurs = array.array('i')
# nbre_valeurs = int(input("Combien de valeurs entrerez-vous? "))
# max = 0
#
# for i in range(0, nbre_valeurs):
#     a = int(input("Valeur {} : ".format(i)))
#     if a > max:
#         max = a
#
# print("Le maximum des valeurs est : ", max)


'''
TABLEAU DE NOTES
'''
# import array as ar
#
#
# nbre_etudiants, som_notes = int(input("Combien d'etudiants gerez-vous? ")), 0
# notes_etudiants = ar.array('i')
#
# for i in range(0, nbre_etudiants - 1):
#     notes_etudiants[i] = int(input("Entrez la note de l'etudiant {} : ".format(i)))
#     som_notes += notes_etudiants[i]
#
# moy_notes = som_notes / nbre_etudiants
#
# for i in notes_etudiants:
#     if notes_etudiants[i] > moy_notes:
#         print("L'etudiant {} a la note {}", format(i, notes_etudiants[i]))

