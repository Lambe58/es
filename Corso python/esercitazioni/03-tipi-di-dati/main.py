#tipi di dati

# i tipi di dati semplici

# variabili di tipo intero
eta = 10 # dichiarazione e inizializzaione di una variabile intera

# variabile di tipo decimale
altezza = 1.70 # dichiarazione e inizializzazione di una variabile float

# variabili di tipo di carattere
inizale = 'M' # dichiarazione e inizializzazione di una variabile carattere

# variabili di tipo stringa
nome="nome1"  # dichiarazione e inizializzazione di una variabile stringa

# variabili di tipo boleano
maggiorenne = True # dichiarazione e inizializzazione di una variabile booleana

# variabili di tipo data
from datetime import datetime # importo il modulo datetime
data_nascita = datetime(2000, 1, 1) # dichiarazione e inizializzazione di una variabile datetime (anno, mese, giorno)
#utilizzo delle variabili con interpolazione di stringhe (f-string)
print(f"la variabile eta contiene il valore {eta}")  #Outout: la variabile eta contiene il valore 10
print(f"la variabile altezza contiene il valore {altezza}") #Output: la variabile altezza contiene il valore 1.7

# i tipi di dati complessi (o strutture di dati)

# ARRAY (con la libreria array)
import array # importo il modulo array
numeri = array.array('i', [10, 20, 30, 40,50]) #dichiarazione e inizializzaione di un array di interi
# uso array.array perchè è una libreria che ha un metodo che si chiama allo stesso modo
# 'i' indica che gli elementi dell'array sono numeri interi
# stampo l'array
print(numeri)  #Outpu: array ('i', [10, 20, 30, 40, 50])
# aggiunta di un elemento all'array
numeri.append(69) # aggiunta di un elemento alla fine dell'array
# stampo l'array
print(numeri)  # output: array('i', [10, 20, 30, 40, 50, 60])
# stampo attraverso un ciclo for
for numero in numeri:
    print(numero) # stampo ogni elemento

# lista
numeri_lista = [10, 20, 30, 40, 50] #Dichiarazione e inizializzazione di una lista di interi
numeri_lista.append(60) # aggiunta di un elemento alla lista
#stampo la lista
print(numeri_lista) #output: [10, 20, 30, 40, 50]
# stampo attraverso un ciclo for
for numero in numeri_lista:
    print(numero) #Output 10 20 30 40 50 60

#lista di stringhe
nomi_lista = ["nome1", "nome2", "nome3"]  #dichiarazione e inizializzazione di una lista di stringhe
# una lista può contenere elementi di diverti tipi
lista_mista = [10, "nome1", 20.5, True]
# stampo attraverso un ciclo for
for (elemento) in lista_mista:
    print(elemento) #Output: 10 nome1 20.5 True

#dizionario
voti= {"matematica": 28, "informatica": 30}  #dichiarazione e inizializzazione di un dizionario
print(voti)
voti["fisica"] = 26 #output: {'matematica': 28, 'informatica':30, 'fisica': 26}
# stampo il dizionario
print(voti) #Output {'matematica': 28, 'informatica': 30, 'Fisica':26}

# Esempi di utilizzo delle strutture dati
print(f"il primo numero della lista è: {numeri_lista[0]}") #Output: il primo della lista è: 10
print(f"il voto in matematica è: {voti['matematica']}") #output: il voto in matematica è: 28

#best practices per la dichiarazione di variabili
# - usa nomi sigificativi
# - segui la convenzione snake_case per i nomi delle variabili

# esempio di variabili dichiarate con nomi significativi
eta_studente = 20
altezza_media_studenti = 1.75
is_maggiorenne = True



