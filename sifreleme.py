import hashlib
from Crypto.Cipher import DES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
class sifreleme():
    def __init__(self,metin1):
        self.metin = metin1
 
    def md5(self):
        paragraf = self.metin
        paragraf = str(paragraf)
        sifrelenecek = paragraf.encode("utf-8")
        sifreleyici = hashlib.md5()
        sifreleyici.update(sifrelenecek)
        
        return print("MD5: "+ sifreleyici.hexdigest())
    
    def sha1(self):
        paragraf = self.metin
        paragraf = str(paragraf)
        sifrelenecek = paragraf.encode("utf-8")
        sifreleyici = hashlib.sha1()
        sifreleyici.update(sifrelenecek)
        
        return print("SHA1: "+ sifreleyici.hexdigest())
    
    def sha224(self):
        paragraf = self.metin
        paragraf = str(paragraf)
        sifrelenecek = paragraf.encode("utf-8")
        sifreleyici = hashlib.sha224()
        sifreleyici.update(sifrelenecek)
        
        return print("sha224: "+ sifreleyici.hexdigest())

    def sha256(self):
        paragraf = self.metin
        paragraf = str(paragraf)
        sifrelenecek = paragraf.encode("utf-8")
        sifreleyici = hashlib.sha256()
        sifreleyici.update(sifrelenecek)
        
        return print("sha256: "+ sifreleyici.hexdigest())
    
    def sha384(self):
        paragraf = self.metin
        paragraf = str(paragraf)
        sifrelenecek = paragraf.encode("utf-8")
        sifreleyici = hashlib.sha384()
        sifreleyici.update(sifrelenecek)
        
        return print("sha384: "+ sifreleyici.hexdigest())

    def sha512(self):
        paragraf = self.metin
        paragraf = str(paragraf)
        sifrelenecek = paragraf.encode("utf-8")
        sifreleyici = hashlib.sha512()
        sifreleyici.update(sifrelenecek)
        
        return print("sha512: "+ sifreleyici.hexdigest())
        
    def des(self):
        def pad(text):
            n = len(text) % 8
            return text + (b' ' * n)
        key = b'hello123'
        text1 = b'Python is the Best Language!'
        des = DES.new(key, DES.MODE_ECB)

        padded_text = pad(text1)
        encrypted_text = des.encrypt(padded_text)
        encrypted_text = str(encrypted_text)

        return print('DES: {}'.format(encrypted_text))
    
    def rsa(self):
        key = RSA.generate(2048)
        public_key = key.publickey().exportKey('PEM')
        message = self.metin
        message = str.encode(message)

        rsa_public_key = RSA.importKey(public_key)
        rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
        encrypted_text = rsa_public_key.encrypt(message)

        return print('RSA: {}'.format(encrypted_text))


sfr = sifreleme("furkan")
sfr.md5()
sfr.sha1()
sfr.sha224()
sfr.sha256()
sfr.sha384()
sfr.sha512()
sfr.des()
sfr.rsa()

