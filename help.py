
class help():
    def __init__(self):
        sayac = 0
    for i in range(4):
        print("Sifreleme modülü hakkında bilgi almak içim 1'e Dil kontrol modülü hakkında bilgi almak için 2'yi tuşlayınız: ")
        x = input()
        if x == '1':
            print("sifreleme modulü 8 adet fonksiyon içermektedir.\n"
            +"Bunlar sırayla:\n 1-MD5 \n 2-SHA1 \n 3-SHA224 \n 4-SHA256 \n"+
            " 5-SHA384 \n 6-SHA512 \n 7-DES \n 8-RSA \n"+
            "1-MDA5:\n"+
            "İlk önce metnimizi " 
            +"oluşturduk.Daha sonra import hashlib Kütüphanemizin"
            +"bize sunduğu şifreleme algoritmaların md5 şifreleyicimizi seçtik"+
            "ve ardından verimizi update() fonksiyonuyla şifreledik."+
            "verilerimizin şifrelenmiş haline ulaşmak içinde sifreleyici.digest() fonksiyonunu kullandık.\n"+
            
            "\n2-SHA1:\n "+
            "İlk önce metnimizi "  
            +"oluşturduk.Daha sonra import hashlib Kütüphanemizin"
            +"bize sunduğu şifreleme algoritmaların sha1 şifreleyicimizi seçtik"+
            "ve ardından verimizi update() fonksiyonuyla şifreledik."+
            "verilerimizin şifrelenmiş haline ulaşmak içinde sifreleyici.digest() fonksiyonunu kullandık.\n"

            +"\n3-SHA224:\n" +
            "İlk önce metnimizi " 
            +"oluşturduk.Daha sonra import hashlib Kütüphanemizin"
            +"bize sunduğu şifreleme algoritmaların sha224 şifreleyicimizi seçtik"+
            "ve ardından verimizi update() fonksiyonuyla şifreledik."+
            "verilerimizin şifrelenmiş haline ulaşmak içinde sifreleyici.digest() fonksiyonunu kullandık.\n"
            
            +"\n4-SHA256\n "+
            "İlk önce metnimizi " 
            +"oluşturduk.Daha sonra import hashlib Kütüphanemizin"
            +"bize sunduğu şifreleme algoritmaların sha256 şifreleyicimizi seçtik"+
            "ve ardından verimizi update() fonksiyonuyla şifreledik."+
            "verilerimizin şifrelenmiş haline ulaşmak içinde sifreleyici.digest() fonksiyonunu kullandık.\n"
            
            +"\n5-SHA384:\n "+
            "İlk önce metnimizi " 
            +"oluşturduk.Daha sonra import hashlib Kütüphanemizin"
            +"bize sunduğu şifreleme algoritmaların sha384 şifreleyicimizi seçtik"+
            "ve ardından verimizi update() fonksiyonuyla şifreledik."+
            "verilerimizin şifrelenmiş haline ulaşmak içinde sifreleyici.digest() fonksiyonunu kullandık.\n"
            
            +"\n6-SHA512:\n "+
            "İlk önce metnimizi" 
            +"oluşturduk.Daha sonra import hashlib Kütüphanemizin"
            +"bize sunduğu şifreleme algoritmaların sha512 şifreleyicimizi seçtik"+
            "ve ardından verimizi update() fonksiyonuyla şifreledik."+
            "verilerimizin şifrelenmiş haline ulaşmak içinde sifreleyici.digest() fonksiyonunu kullandık.\n")
            
            
            break
        elif x == '2':
            print("Dilkontrol modulü 5 adet fonksiyon içermektedir.\n"+   
            "Bunlar sırayla:\n 1-Metni kelimelere ayırma \n 2-metni cümlelere ayırma \n 3-sesli harf arama \n 4-büyük ünlü uyumu \n"+
            " 5-küçük ünlü uyumu\n"+
            "\n1-Metni kelimelere ayırma:\n"+
            "İlk olarak 2 tane sayac tutulur. Sonrasında while döngüsü ilk tutlan sayacın metin karakter uzunluğundan "+
            "büyük olana kadar çalışması için ayarlanır.Döngüde var olan sayac değişkeni if bloğunda metindeki karakterleri "+
            "teker teker gezer ve boşluk karakterini bulmaya çalışır.Boşluk karakterini bulduktan sonra sayac1 i bir arttırır"+
            "elif bloğu ise cümlenin sonuna gelinip gelinmediğini kontrol eder. eğer cümlenin sonuna gelinmişse sayac1 i bir arttırır."+
            "son olarak da sayac1 değişkeni geri döndürülür.\n"

            "\n2-Metni cümlelere ayırma:\n"+
            "İlk olarak 2 tane sayac tutulur. Sonrasında while döngüsü ilk tutlan sayacın metin karakter uzunluğundan "+
            "büyük olana kadar çalışması için ayarlanır.Döngüde var olan sayac değişkeni if bloğunda metindeki karakterleri "+
            "teker teker gezer ve nokta karakterini bulmaya çalışır. Nokta karakterini bulduktan sonra sayac1 i bir arttırır"+
            "Son olarak da sayac1 değişkeni geri döndürülür.\n"
            
            "\n3-Sesli Harf sayma:\n"+
            "İlk olarak sesli harfler bir değişkene atanır ve sayac değişkeni tutulur. Sonrasında for döngüsü oluşturularak i değişkeni"+
            "metnin içerisindeki harfjeri teker teker gezer. İf bloğunda ise döngüdeki di değişkeni içinde sesli harf olan sesliharfler değişkeninni kontrol eder. "+
            "if bloğunun durumu true olursa sayacı bir arttırır.Son olarak da sayac1 değişkeni geri döndürülür.\n"
            
            "\n4-Küçük ünlü uyumu:\n"+
            "İlk olarak 2 tane sayac ve metindeki kelimeleri ayırıp bir listeye atmak için split metodu kullanılır."+
            "for word in splitWords: döngüsü açılarak döngü içinde bulunan if word not in allWords: bloğu altında allWords.append(word) diye yazılır."+
            "for döngüsündeki word değişkeni split fonksiyonu kullanılarak kelimelere ayrılmış metindeki kelimelerin yerini tutar."+
            "if bloğunda ise kelime listede daha önce varmı yokmu diye kontrol ettirilir. İf bloğu true döndürürse append fonksiyonu kullanarakta boş listeye tuttuğu değeri yazdırır"+
            "Sonrasında unluler diye liste oluşturulup içine ünlü harfler atılır. For döngüsü açılır ve boş bir liste oluşturulur. Sonraki for döngüsünde kelime içerisindeki ünlüleri oluşturduğumuz boş "+
            "listeye atarız. düz ünlüler,düzden sonra gelecek unluler, yuvarlak ünlüler, yuvarlak unlulerden sonra gelicek unluler olmak üzere 4 liste ve 1 deişken oluşturulur."+
            "Sonrasında for döngüsü içerisinde küçük ünlü uyumuna uyuyorsa son tutlan değişkene true uymuyorsa false değeri döndürülür. Değişken değeri sıradaki if bloğu tarafından kontrol edilir kurala uyuyorsa sayac 1arttırılır uymuyarsada sayac1 bir arttırılır"+
            "büyük olana kadar çalışması için ayarlanır.Döngüde var olan sayac değişkeni if bloğunda metindeki karakterleri "+
            "Son olarak da sayac1 ve sayac değişkeni geri döndürülür.\n"
            
            "\n5-Büyük Ünlü uyumu:\n"+
            "İlk olarak 2 tane sayac ve metindeki kelimeleri ayırıp bir listeye atmak için split metodu kullanılır."+
            "for word in splitWords: döngüsü açılarak döngü içinde bulunan if word not in allWords: bloğu altında allWords.append(word) diye yazılır."+
            "for döngüsündeki word değişkeni split fonksiyonu kullanılarak kelimelere ayrılmış metindeki kelimelerin yerini tutar."+
            "Kalın ünlüler, ince unluler olmak üzere 2 liste  oluşturulur."+
            "Sonrasında for döngüsü içerisinde if bloğu tarafından kontrol edilir kurala uyuyorsa sayac bir arttırılır uymuyarsada sayac1 bir arttırılır"+
            "büyük olana kadar çalışması için ayarlanır.Döngüde var olan sayac değişkeni if bloğunda metindeki karakterleri "+
            "Son olarak da sayac1 ve sayac değişkeni geri döndürülür.\n")
            
            break
        else:
            print("Yanlış tuşlama yaptınız lütfen tekrarlayınız.")
            sayac = sayac +1
            continue
    else:
        print("3 ten fazla hatalı tuşlama yaptınız devam etmek için bir tuşa basınız.")


        
helped = help()
