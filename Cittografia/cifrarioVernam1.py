'''lista = [
    a = 0,
    b = 1,
    c = 2,
    d = 3,
    e = 4,
    f = 5,
    g = 6,
    h = 7,
    i = 8,
    j = 9,
    k = 10,
    l = 11,
    m = 12,
    n = 13,
    o = 14,
    p = 15,
    q = 16,
    r = 17,
    s = 18,
    t = 19,
    u = 20,
    v = 21,
    w = 22,
    x = 23,
    y = 24,
    z = 25,
]
'''

chiave = input(f'Scrivi qui il tuo messaggio: ')
print('Il messaggio da cifrare è: ', chiave)

chiave = chiave.lower()

output = ['Il messaggio cifrato è: '] 

for character in chiave:
    chiave1 = chiave.split()
    numero = ord(character) - 96
    output.append(numero) 

print(output)

risultato = output % 96
print(risultato)



