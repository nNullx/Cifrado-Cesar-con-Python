alf =  ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
ind = ["Valores no deseados: "]
#Copyright on nNullx
def ces(n, w):
    l = len(w); o = 1; p = 0; f = 0; x = w
    if n == "t":
        while o <= 26:
            x = w
            x = enc(x, l, f, o, p)
            print("Encriptado (Clave:", o, ") " + x)
            o += 1 
        lim(x, l, p, 1, "Encriptado")
    else:
        while n > 26:
            n -= 26
        print("Desencriptado: " + w)
        r = enc(w, l, f, n, p)
        print("Encriptado: " + r)
        lim(r, l, p, 0, "Encriptado")
        esp(r, "e")
#Copyright on nNullx
def ces2(n, w):
    l = len(w); o = 1; p = 0; f = 0; x = w
    if n == "t":
        while o <= 26:
            x = w
            x = des(x, l, f, o, p)
            print("Desencriptado (Clave:", o, ") " + x)
            o += 1 
        lim(x, l, p, 1, "Desencriptado")
        esp(x, "d")
    else:
        while n > 26:
            n -= 26
        print("Encriptado: " + w)
        r = des(w, l, f, n, p)
        print("Desencriptado: " + r)
        lim(r, l, p, 0, "Desencriptado")
        esp(r, "d")
#Copyright on nNullx
def enc(x, l, f, o, p):
    i = 0
    while i < l:
        try:
            p = alf.index(x[i])
        except:
            i += 1
            continue
        if p == 104:
            i += 1
            continue
        f = alf[p + o]
        x = x[:i] + f + x[i+1:]
        i += 1
    return x
#Copyright on nNullx
def des(x, l, f, o, p):
    i = 0
    while i < l:
        try:
            p = alf.index(x[i])
        except:
            i += 1
            continue
        if p == 104:
            i += 1
            continue
        f = alf[(p + (26 - o))]
        x = x[:i] + f + x[i+1:]
        i += 1
    return x
#Copyright on nNullx
def esp(w, j):
    s = 0; v = w
    if w.find(" ") == -1:
        return
    while True:
        if w[0] == " ":
            w = w[1:]
            continue
        if w[len(w) - 1] == " ":
            w = w[:len(w) - 1]
            continue
        break
    while True:
        i = w.find(" ", s + 1)
        if i == -1:
            break
        if w[i] == w[i + 1]:
            w = w[:i] + "" + w[i+1:]
            continue
        s = i
    if v != w:
        if j == "e":
            print("Encriptado(Espaciado): " + w)
        else:
            print("Desencriptado(Espaciado): " + w)
#Copyright on nNullx
def lim(v, l, p, s, d):
    i = 0
    w = v
    while i < l:
            try:
                p = alf.index(v[i])
                i += 1
            except:
                ind.append(v[i])
                v = v[:i] + v[i+1:]
                l -= 1
    if v != w and s == 0:
        print(d + "(Limpio): " + v)
    if len(ind) != 1:
        print(ind)

tip = str(input("Encrypt(E) or Desencypt(D)?: ")).lower()
#Copyright on nNullx
if tip == "e" or tip == "encriptar" or tip == "encrypt":
    num = str(input("Key: ")).lower()
    if num.find("all") > -1 or num.find("todo") > -1:
        wrd = input("String: ")
        ces("t", wrd)
    else:
        try:
            num = int(num)
            wrd = input("String: ")
            ces(num, wrd)
        except ValueError:
            print("Introduce un valor valido ")
if tip == "d" or tip == "desencriptar" or tip == "desencrypt":
    num = str(input("Key: ")).lower()
    if num.find("all") > -1 or num.find("todo") > -1:
        wrd = input("String: ")
        ces2("t", wrd)
    else:
        try:
            num = int(num)
            wrd = input("String: ")
            ces2(num, wrd)
        except ValueError:
            print("Introduce un valor valido ")