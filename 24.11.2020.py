# sayı tahmin oyunu
#24.11.2020
import random 

tahmin_no=1
sayi= random.randint(1,100)                           #bilgisayar [1-100] arasında sayı tutuyor 
                                                                           #bilgisayarın tuttuğu sayı ( biz bilmiyoruz )
tahmin=int(input("1. tahmininiz nedir "))        #sayı tahmin değerine eşit değil ise !=
while sayi!=tahmin:
    if sayi <tahmin:
        print("benim sayım daha küçük")
    elif sayi>tahmin:
        print("benim sayım daha büyük")
    tahmin_no=tahmin_no+1
    print(tahmin_no,".tahmininiz nedir",end=' ') #end=' ' ile satırda kalması 
    tahmin=int(input("" )) 

print("tebrikler! sayımı ",tahmin_no,". tahmininizde bildiniz ")
print("benim tuttuğum sayı da",sayi," idi")
print("güle güle")

#binary search ikili arama 

