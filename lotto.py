import random

originNumbers=[]
tippedNumbers=[]
chosenNumber=[]

def setOriginList():
    for i in range(1,91):
        originNumbers.append(i)
    print(originNumbers)


def tipp(tippedNumbers):
    for i in range(0,5):
        number=int(input("szám: "))
        tippedNumbers.append(number)

    tippedNumbers=sortList(tippedNumbers)    
    print(tippedNumbers)



def sortList(l):
    lista=l
    for i in range(len(lista)-1,0,-1):
        for j in range(0,i):
            if(lista[j]>lista[j+1]):
                tmp=lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=tmp 
    return lista     



def choosing(chosenNumber):
    for i in range(0,5):
        index=random.randrange(0,len(originNumbers))
        number=originNumbers[index]
        chosenNumber.append(number)
        originNumbers.pop(index)  
    chosenNumber=sortList(chosenNumber)    
    print(chosenNumber)

setOriginList()     
# choosing()   
tipp(tippedNumbers)