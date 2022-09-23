angka=int(input("input angka = "))

if angka%2==0 and angka!=0:
    print("genap")
elif angka==0:
    print("angka 0")
else:
    print("ganjil")


#statement if condition else statement
print("genap" if angka%2==0 else "ganjil")  


#tuple (false, true)[condition]
pesan=("ganjil","genap")[angka%2==0]
print(pesan)

pesan=(("nol","negatif")[angka<0],"Positif")[angka>0]
print(pesan)

try:
    hasil=10/angka
    print("hasil: " ,hasil)
except ZeroDivisionError as e:
    print("eror: ",e)
    print("jangan bagi dengan nol")
    hasil=10/1
except NameError as e:
    print("error : ",e)
else:
    print("tidak ada eror")
finally:
    print(hasil)