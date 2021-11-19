#input
bar1 = float(input("Masukkan besar RSI :"))
bar2 = str(input("Masukkan kondisi MACD :"))

#menampilkan output
if (bar1 >= 70) and (bar2 == 'golden-cross'):
        kt="lebih dari sama dengan 70"
        hj="Tunggu MACD sampai death-cross"
elif (bar1 <= 30) and (bar2 == 'death-cross'):
        kt="kurang dari sama dengan 30"
        hj="Tunggu MACD sampai golden-cross"
elif (bar1 <= 30) and (bar2 == 'golden-cross'):
        kt="kurang dari sama dengan 30"
        hj="saatnya Beli"
elif (bar1 >= 70 ) and (bar2 == 'death-cross'):
        kt="lebih dari sama dengan 70"
        hj="saatnya Jual"
if (bar1 >= 70) or (bar1 <= 30):
    print("RSI",kt, "dan MACD",bar2,",",hj)
else :
    kt="berada di area 30-70"
    hj="Bukan saatnya membeli maupun menjual"
    print("RSI",kt,",",hj)