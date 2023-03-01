def aritmatika(a,b,n):
    c = (n/2)*((2*a)+(n-1)*b)
    return c

a = int (input("Masukan suku pertama\n>> "))
b = int(input("Masukan selisih\n>> "))
n = int(input("Masukan banyaknya suku\n>> "))

print(aritmatika(a,b,n))