#SANTAROSSA RICCARDO 

v1= input("Inserisci il primo voto \n")
v2= input("Inserisci il secondo voto \n")
v3= input("Inserisci il terzo voto \n")

media = (float(v1)+float(v2)+float(v3))/3

if media<3:
    print("Giudizio: NULLO")
elif media >= 3 and media<4.5:
    print("Giudizio: GRAVEMENTE INSUFFICIENTE")
elif media >=4.5 and media<6:
    print("Giudizio: INSUFFICIENTE")
elif media >= 6 and media<7.5:
    print("Giudizio: SUFFICIENTE")
elif media >= 7.5 and media<9:
    print("Giudizio: BUONO")
elif media >9:
    print("Giudizio: ECCELLENTE")




