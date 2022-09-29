print("INPUT")
nama = input("Masukan Nama : ")
npm = input("Masukan NPM : ")
nilai = eval(input("Masukan Nilai : "))

def hm(nilai):
    if(nilai >= 76 and nilai <= 100):
        hurufmutu = "A"
    elif(nilai >= 71 and nilai < 76):
        hurufmutu = "B+"
    elif(nilai >= 66 and nilai < 71):
        hurufmutu = "B"
    elif(nilai >= 61 and nilai < 66):
        hurufmutu = "C+"
    elif(nilai >= 56 and nilai < 61):
        hurufmutu = "C"
    elif(nilai >= 50 and nilai < 56):
        hurufmutu = "D"
    elif(nilai < 50 and nilai >= 0):
        hurufmutu = "E"
    else:
        hurufmutu = "Input Salah"
    return hurufmutu

def cetak():
    print("\nOUTPUT")
    print("Nama : ", nama)
    print("NPM : ", npm)
    print("Huruf Mutu : ", hm(nilai))

cetak()