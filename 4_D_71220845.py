deret = (input("Masukan deret angka anda (Pisahkan dengan koma)\n>> ")).split(",")
pnjg = len(deret)
a = deret.sort(key = lambda deret : int(deret))
maksimum = deret[pnjg-1]
minimum = deret[0]
print (f"Angka terbesar adalah {maksimum}\nAngka terkecil adalah {minimum}")