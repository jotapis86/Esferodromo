def separadorMiles(n):
    """Formatea los numeros para presentarlos con '.' en separacion de miles"""
    # float --> str
    s = str(n)
    cont = 1
    part = s.split(".")
    if len(part) == 1:
        sn = ""
    else:
        sn = ","+part[1]
    s = part[0]
    i = len(s)
    while i > 0:
        if cont % 4 == 0 and s[i-1] != "-":
            sn = s[i-1] + "." + sn
            cont = 2
        else:
            sn = s[i-1] + sn
            cont += 1
        i -= 1
    return sn
