print("Selamat Datang di Kalkulator Sederhana")
print("Ketik 1 untuk menghitung penjumlahan.")
print("ketik 2 untuk menghitung pengurangan.")
print("ketik 3 untuk menghitung perkalian")
print("ketik 4 untuk menghitung pembagian")
print("ketik 5 untuk menghitung sisa hasil bagi (modulus)")
print("ketik 6 untuk menghitung pemangkatan")
a = int(input("Masukan Pilihan Anda :"))
b = int(input("Masukan Bilangan Pertama :"))
c = int(input("Masukan Bilangan Kedua :"))
if a == 1 :
    jumlah = b + c
    print ("Hasil dari",b,"dijumlahkan dengan",c,"adalah",jumlah)
elif a == 2 :
    jumlahl = b - c 
    print ("Hasil dari",b,"Dikurangi dengan",c,"adalah",jumlah)
elif a == 3 :
    jumlah = b * c
    print ("Hasil Dari",b,"Dikali dengan",c,"adalah",jumlah)
elif a == 4 :
    jumlah = b / c
    print ("Hasil dari",b,"DiBagi dengan",c,"adalah",jumlah)
elif a == 5 :
    jumlah = b % c
    print ("Hasil dari",b,"Sisa Bagi dengan",c,"adalah",jumlah)
elif a == 6 :
    jumlah = b / c
    print ("Hasil dari",b,"Pemangkatan dengan",c,"adalah",jumlah)
else :
    print ("raiso")
    
