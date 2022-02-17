#SANTAROSSA RICCARDO


from re import A


tipoVeicolo = input("Inserisci il tipo di veicolo \n")
cilindrata = input("Inserisci la cilindrata del veicolo \n")

if tipoVeicolo == "Auto" or tipoVeicolo == "a" or tipoVeicolo == "A":
    if int(cilindrata) <=1000:
        print("Il costo del biglietto è di 20€")
    elif int(cilindrata) >1000 and int(cilindrata)<=2000:
        print("Il costo del biglietto è di 30€") 
    else:
        print("Il costo del biglietto è di 50€")
elif tipoVeicolo == "Camion" or tipoVeicolo == "c" or tipoVeicolo == "C":
    if int(cilindrata) <=2000:
        print("Il costo del biglietto è di 40€")
    elif int(cilindrata) >2000 and int(cilindrata)<=3000:
        print("Il costo del biglietto è di 50€") 
    else:
        print("Il costo del biglietto è di 100€")