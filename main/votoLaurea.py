V110 = 0
Vesami = [26.3, 26.4, 26.5, 26.6, 26.7, 26.8, 26.83, 26.9, 26.96, 27, 27.1, 27.2, 27.3, 27.4, 27.5, 27.6]
#Ves = 26.9
Ncfu = 90
VotoTesi = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
VotoLaureaArr = []
for Ves in Vesami:
    print("Media = ", Ves)
    for Vts in VotoTesi:
        V110 = ((Ves * Ncfu) + (Vts * 30))/120
        V110 = round(V110 * (110 / 30))
        # print("Voto senza bonus: ", V110)

        if V110 <= 90:
            delta1 = 0
        elif (V110 > 90) and (V110 <= 106):
            delta1 = (V110 - 90)/4
        elif V110 > 106:
            delta1 = 4
        delta2 = 0
        VotoLaurea = round(V110 + delta1 + delta2)
        VotoLaureaArr.append(VotoLaurea)
        # print("Voto di laurea: ",VotoLaurea)
    maxVoto = max(VotoLaureaArr)
    #print(VotoLaureaArr)
    prova = []
    for i in range(len(VotoTesi)):
        coppia = [VotoTesi[i], VotoLaureaArr[i]]
        prova.append(coppia)
    print(prova)
    VotoLaureaArr = []
    print("Voto massimo raggiungibile: ", maxVoto)
    print("-" * 150)
