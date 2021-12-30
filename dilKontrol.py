
class dilKontrol():
    def __init__(self,metin1):
        self.metin = metin1
        print(self.metin)
 
    def kelimelereAyir(self):
        sayac=0
        sayac1 = 0
        while sayac < len(self.metin):
            if self.metin[sayac] == " ":
                sayac1 += 1
            elif sayac == len(self.metin) - 1:
                sayac1 += 1
            sayac += 1
        return print(str(sayac1) + " kelime var")

    def cumlelereAyir(self):
        sayac=0
        sayac1 = 0
        while sayac < len(self.metin):
            if self.metin[sayac] == ".":
                sayac1 += 1
            sayac += 1
        return print(str(sayac1) + " cümle var")
       
    def sesliHarfSayisi(self):
        sesli_harf = 'AEIİOÖUÜaeıioöuü'
        sayac = 0
        for i in self.metin:
            if i in sesli_harf:
                sayac += 1
        return print(str(sayac) + " sesli harf var")
 
    def kucukUnluUyumu(self):
        sayac = 0
        sayac1 = 0
        splitWords = self.metin.split()
        allWords=[]
        for word in splitWords:
            if word not in allWords:
                allWords.append(word)
        
        unluler = list("AIOUEİÖÜaıoueiöü")  
        for word in allWords:
            kiu = []  
            for harf in word:
                if harf in unluler:
                    kiu.append(harf)  
            duz_unluler = list("aeıi")  # veya ['a', 'e', 'ı', 'i']. Düz ünlüden sonraki ünlü yine bu liste içerisinde olmalıdır.
            duzden_sonra = list("aeıi")
            yuvarlak_unluler = list("ouöü")  # veya ['o', 'u', 'ö', 'ü'] Yuvarlak ünlüden sonraki ünlü a, e, u, ü olmalıdır.
            yuvarlaktan_sonra = list("aeuü")
            kurala_uyuyor = None
            for indeks in range(len(kiu)):
                try:
                    if kiu[indeks] in duz_unluler and kiu[
                        indeks + 1] in duzden_sonra:  # Mevcut ünlü ve bir sonra gelen ünlü kurala uyuyor mu diye bakar.
                        
                        kurala_uyuyor = True
                    elif kiu[indeks] in yuvarlak_unluler and kiu[
                        indeks + 1] in yuvarlaktan_sonra:  # Mevcut ünlü ve bir sonra gelen ünlü kurala uyuyor mu diye bakar.
                        
                        kurala_uyuyor = True
                    else:
                        kurala_uyuyor = False
                        break  # Tekrar tekrar çıktı almamak metinına döngüyü durdururuz.
                        
                except IndexError:  # kiu'nun son elemanına geldiğinde kendisinden bir sonraki elemana bakamayacağından hata verecektir. Bu yüzden error exception kullandık.
                    continue  # Hatayı aldıktan sonra devam eder.

            if kurala_uyuyor:
                sayac += 1
            else:
                sayac1 += 1
        return print(str(sayac)+ " Kelime küçük ünlü uyumuna uyar" +"\n"+ str(sayac1)+ " Kelime küçük ünlü uyumuna uymaz")
        
    def buyukUnluUyumu(self):
        sayac = 0
        sayac1 = 0
        splitWords = self.metin.split()
        allWords=[]
        for word in splitWords:
            if word not in allWords:
                allWords.append(word)
        kalin_unluler = list("aıou") 
        ince_unluler = list("eiöü")  
        for word in allWords:
            if (sum(word.count(kalin) for kalin in kalin_unluler)) != 0 and (sum(word.count(ince) for ince in ince_unluler)) != 0:  # Aynı kelime içerisinde hem kalın ünlü hem de ince ünlü bulunuyor mu diye bakar.
                sayac1 += 1
            else:
                sayac += 1

        return print(str(sayac)+ " Kelime büyük ünlü uyumuna uyar" +"\n"+ str(sayac1)+ " Kelime büyük ünlü uyumuna uymaz")
            
tdk = dilKontrol("Karanlıkta arkadaşlarım ali kadir ile yogurt tükettim. Sonrada yağmur çamur demeden kavun yedik.")
tdk.kelimelereAyir()
tdk.cumlelereAyir()
tdk.sesliHarfSayisi()
tdk.buyukUnluUyumu()
tdk.kucukUnluUyumu()