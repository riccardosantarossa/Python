#SANTAROSSA RICCARDO 

while True:
    nColonne = int(input("Inserisci il numero di colonne del rettangolo \n"))
    nRighe = int(input("Inserisci il numero di righe del rettangolo \n"))
    if int(nColonne)> 3 and int(nRighe)>3:
        break

for i in range(nRighe):
    print('*' ,end=' ') 
    for j in range(nColonne-2):
        if i == 0 or i == nRighe-1:
            print('*' ,end=' ') 
        else: 
            print('Q', end=' ')
    print('* \n') 

 