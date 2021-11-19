#input
angka = int(input("Masukkan angka :"))

#menampilkan output
if (angka%2) == 0 and (angka%3) !=0:
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: Ya")
    print(" ")
    if (angka%5 != 0) or (angka%10 == 0):
        print("Apakah bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: IYA DONG")
    elif (angka%5 == 0) or (angka%10 != 0):
        print("Apakah bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: TIDAK")
else :
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")