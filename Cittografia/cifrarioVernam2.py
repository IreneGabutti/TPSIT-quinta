
message = input(f"inserisci: ")
print('messaggio cifrato', message)

key = "itisdelpozzo"

def vernam(key,message):
    message = str(message)
    m = message.upper().replace(" ","") 
    encrypt = ""
    try:
        key = int(key)           
    except ValueError:
        key = 0
    for i in range(len(m)):
        letter = ord(m[i])-65      
        letter = (letter + key)%25 
        letter +=65
        

        encrypt = encrypt + chr(letter) 
        
    return encrypt
    
