def crikata (kal1):
    pnjg = len(kal1)
    a = 1
    b = 2
    e = 1
    while e <= pnjg:
        c = len(kal1[a])
        d = len(kal1[b])
        if c > d:
            b+=1
            e+=1
            max1 = kal1[a] 
        else:
            a+=1
            e+=1
            max1 = kal1[b]
    return max1

kal = str(input("Masukan kalimat anda\n>> ")).split(" ")
akhir = crikata(kal).title()
print (f"Kata terpanjang adalah {akhir}")