#input
a = str(input("Masukkan nilai huruf PrakTekKom anda :"))
b = input("=================================")

#menampilkan output
jk="Rentang nilai PrakTekKom anda adalah"
if a == 'A':
    print(jk,"85 - 100")
elif a == 'A-':
    print(jk,"80 - 84")
elif a == 'B+':
    print(jk,"75 - 79")
elif a == 'B':
    print(jk,"70 - 74")
elif a == 'B-':
    print(jk,"65 - 69")
elif a == 'C+':
    print(jk,"60 - 64")
elif a == 'C':
    print(jk,"55 - 59")
elif a == 'D':
    print(jk,"45 - 54")
elif a == 'E':
    print(jk,"0 - 44")
else :
    print("Inputan anda salah atau nilai huruf tidak ada pada Standar Nilai")