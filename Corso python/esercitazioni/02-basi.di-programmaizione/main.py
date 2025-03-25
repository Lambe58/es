# medoti di inpt e print

"""
i metodi di input e print in python permettono di gestire l'output e l'input

 (il dialogo con l'utente) attraverso la console

"""

# il metodo print()
print("hello world!") # stampa a video la stringa "hello world"

# il metodo input() legge una riga di testo da tastiera e la restituisce come stringa
nome = input("inserisci il tuo nome: ")
#stampo il nome inserito
print("ciao", nome )
#eseguo lo script con python main.py

# Stampo il nome concatenato con una stringa
print("ciao " + nome + "!")  #Con il segno + posso concatenare stringhe con variabili

# Stampo il nome concatenato con una stringa utilizzando l'interpolazione (f-string)
print(f"ciao {nome}!")

# chiedo all'utente di inserire il proprio cognome
cognome= input("cognome: ") #leggo il cognome da tastiera e lo assegno alla variabile 'cognome'

#stampo il nome completo con interpolazione
print(f"ciao {nome} {cognome}!") #con l'interpolazione posso concatenare piu variabili in modo semplificato

#dichiaro una variabile intera eta_int
eta_int ="47" # inizializzo la variabile eta_int con il valore 47

# stampo eta provando anche se è un intero 
print(eta_int) #stampo la variabile eta_int

#dichiaro una variabile stringa eta_str
eta_str = str(eta_int)  #converto l'intero in stringa

# leggo un input con una pausa per simulare ReadKey
print("premi un tasto per continuare")
# metto limport in questa riga per prova ma dovrebbe essere messo all'inizio del file
import msvcrt #Moduo per leggere un singolo tasto su windows
tasto = msvcrt.getch () # legge il tasto premuto

# se il tasto premuto è Enter
if tasto == b'\r': #'\r' rappresenta il tasto enter perche '\r' è il codice ASCII del tasto enter
    # b indica che è un byte cioè un carattere ASCII
    print("hai premuto il tasto enter") # stampo un messaggio
# se il tsto premuto è 's' esco dal programma
if tasto.lower() == b's': # comfronto il tasto convertito in minuscolo con 's'
    print("hai premuto il tasto 's'") #stampo un messaggio
    exit()  # esco dal programma