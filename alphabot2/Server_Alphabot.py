
import socket
import logging 
import _thread
import sqlite3
from os.path import isfile 

#funzione che gestrisce le stampe sul file .log 
def log(x, y, descrizione, tipo):   
    x = str(x)
    y= str(y)
    if tipo == "info":
        logging.info(" " + x + "." + y + ", " + descrizione)
    elif tipo == "warning":
        logging.warning(" " + x + "." + y + ", " + descrizione)
    elif tipo == "error":
        logging.error(" " + x + "." + y + ", " + descrizione)
    elif tipo == "critical":
        logging.critical(" " + x + "." + y + ", " + descrizione)

def conn_client(conn,addr):
    logging.info("INIZIO COMUNICAZIONE CON " + str(addr))
    msg = conn.recv(1024)
    msg = msg.decode("utf-8")
    
    if msg.find(",") == -1:
        log(2, 1 , "Formato messaggi errato", "error")    
        print("Formato messaggi errato")
        rispondiEchiudi(conn, None, "2.1, Formato messaggi errato")
        return -1

    end, start = msg.split(",")

    path = "percorsi.db"
    connDB = None

    #connessione al db
    print()
    if(not isfile(path)):   #controllo che il file percorsi.db esista
        log(4, 1 , "Connessione al db non avvenuta", "critical")    #stampo sul .log un errore generico
        print("Connessione con DB non avvenuta")
        rispondiEchiudi(conn, connDB, "4.1, Connessione al db non avvenuta")
        return -1
    
    connDB = sqlite3.connect(path, check_same_thread=False)
    print("Connessione con DB avvenuta")
    
    #Prima Query
    cursor = connDB.execute("SELECT luoghi.id FROM luoghi WHERE luoghi.nome = ?", (end,))
    
    idEnd = cursor.fetchone() #prende la prima riga della tabella e con '[0]' prendo solo il primo campo, Se eseguo un'altra fetchone() prendo la seconda riga ecc...
    if idEnd is None:
        log(1, 2, "END non trovato", "error")
        print("END non trovato")
        rispondiEchiudi(conn, connDB, "1.2, END non trovato")
        return -1

    idEnd = idEnd[0]

    cursor = None
    cursor = connDB.execute("SELECT luoghi.id FROM luoghi WHERE luoghi.nome = ?", (start,))
    
    idStart = cursor.fetchone()
    if idStart is None:
        log(1, 2, "START non trovato", "error")
        rispondiEchiudi(conn, connDB, "1.2, START non trovato")
        print("Start non trovato")
        return -1
    idStart = idStart[0]
   
    
    print("END: " + str(idEnd))
    print("START: " + str(idStart))

    #Seconda Query 
    cursor = connDB.execute("SELECT inizio_fine.id_percorso FROM inizio_fine WHERE id_start = ? AND id_end = ?", (idStart, idEnd)) 
    idpercorso = cursor.fetchone()

    if idpercorso is None:
        log(1, 1, "Percorso non trovato", "error")
        rispondiEchiudi(conn, connDB, "1.1, Percorso non trovato")
        print("Percorso non trovato")
        return -1

    idpercorso = idpercorso[0]
    print("ID percorso: " + str(idpercorso))

    #terza Query
    cursor = connDB.execute("SELECT percorsi.percorso FROM percorsi WHERE percorsi.id = ?", (idpercorso,)) 
    percorso = cursor.fetchone()[0]
    print("Percorso: " + percorso)

    #invio percorso all'ALPHABOT 
    risposta =  "0.0, " + percorso 
    rispondiEchiudi(conn, connDB, risposta)
    

def rispondiEchiudi(conn, connDB, msg):
    try:
        conn.send(bytes(msg,'UTF-8'))
    except socket.error:
        log(3,1, "Perdita connessione", "critical")
        print("perdita connessione")
   
    conn.close()
    if connDB != None:
        connDB.close()

if __name__ == "__main__":
    s = socket.socket()
    host = "127.0.0.1" 
    port = 50007 

    logging.basicConfig(filename='alphabotServer.log', level=logging.INFO)

    print("inizializzazione")
    print("in attesa di client")


    s.bind((host, port))
    s.listen(5)     #Max 5 Client contemporaneamente 

    while True:
        conn, addr = s.accept() 
        _thread.start_new_thread(conn_client, (conn, addr))
        
    s.close()

    