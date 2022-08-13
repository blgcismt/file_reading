Kalanlar = []
Geçenler = []


def nothesapla(satır):

    satır = satır [:-1]

    liste = satır.split(",")

    isim = liste [0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if(son_not >= 90):
        harf = "AA"
        Geçenler.append(isim + "------------------------------------->" + harf + "\n")
    elif(son_not >= 85):
        harf= "BA"
        Geçenler.append(isim + "------------------------------------->" + harf + "\n")
    elif(son_not >= 80):
        harf = "BB"
        Geçenler.append(isim + "------------------------------------->" + harf + "\n")
    elif (son_not >= 75):
        harf = "CB"
        Geçenler.append(isim + "------------------------------------->" + harf + "\n")
    elif (son_not >= 70):
        harf = "CC"
        Geçenler.append(isim + "------------------------------------->" + harf + "\n")
    elif (son_not >= 65):
        harf = "DC"
        Geçenler.append(isim + "------------------------------------->" + harf + "\n")
    elif (son_not >= 60):
        harf = "DD"
        Geçenler.append(isim + "------------------------------------->" + harf + "\n")
    elif (son_not >= 55):
        harf = "FD"
        Geçenler.append(isim + "------------------------------------->" + harf + "\n")
    else:
        harf = "FF"
        Kalanlar.append(isim + "------------------------------------->" + harf + "\n")
    return isim + "------------------------------------->" + harf + "\n"




with open("dosya.txt","r",encoding = "utf-8")as file:
    eklenecekler = []
    for i in file:
        eklenecekler.append(nothesapla(i))
    with open("notlar.txt","w",encoding = "utf-8") as file2:
        for i in eklenecekler:
            file2.write(i)
    with open("Geçenler.txt", "w", encoding="utf-8") as file3:
        for i in Geçenler:
            file3.write(i)
    with open("Kalanlar.txt", "w", encoding="utf-8") as file4:
        for i in Kalanlar:
            file4.write(i)


