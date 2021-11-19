#input
bil1 = float(input("Masukkan bilangan pertama : "))
bil2 = float(input("Masukkan bilangan kedua : "))
kalimat = str(input("Masukkan kalimat : "))

#proses
switcher = {
    "tambah" : "+" ,
    "kurang": "-",
    "bagi": "/",
    "kali": "*",
}

Kali=bil1*bil2
Kurang=bil1-bil2
Bagi=bil1/bil2
Tambah=bil1+bil2

#menampilkan output
if "kali" in kalimat:
    print("Hasil perkalian",bil1,"dengan",bil2,"adalah", Kali)
elif "bagi" in kalimat:
    print("Hasil pembagian",bil1,"dengan",bil2,"adalah", Bagi)
elif "tambah" in kalimat:
    print("Hasil penjumlahan",bil1,"dengan",bil2,"adalah",Tambah)
else :
    print("Hasil pengurangan",bil1,"dengan",bil2,"adalah", Kurang)



