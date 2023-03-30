import cryptomath, random, hashlib

class Signer:
    
    def __init__(self):
        self.publicKey, self.privateKey = (self.generateInformation())
    
    
    def generateInformation(self):
        p = cryptomath.findPrime()
        q = cryptomath.findPrime()
        phi = (p - 1)*(q - 1)
        n = p*q
        
        print('\n\n') 
        for i in range(40):
            print(" ", end="")
        print("\u001b[1mBlinded signature dan Skema Pemungutan Suara (menggunakan RSA)\u001b[0m")
        for i in range(100):
            print("-", end="")
        print()    
        for i in range(50):
            print(" ", end="")
        print("\u001b[31mLangkah 1\u001b[37m")
        for i in range(100):
            print("-", end="")
        print('\n\n')    
      
        print("\u001b[32;1m1. Admin  Membuat key private dan Pribadi:\u001b[0m", end='\n\n')
        print("\u001b[35;1m(a) Menghasilkan p dan q acak\u001b[0m", end='\n\n')
        print("\u001b[33;1mp: \u001b[0m", p, end='\n\n')
        print("\u001b[33;1mq: \u001b[0m", q, end='\n\n')
        print("\u001b[35;1m(b) Menghitung n = p*q dan ϕ(n) = (p-1)(q-1)\u001b[0m", end='\n\n')
        print("\u001b[33;1mn: \u001b[0m", n, end='\n\n')
        print("\u001b[33;1mϕ(n): \u001b[0m", phi, end='\n\n')
    
    
        print("\u001b[35;1m(c) Memilih e sehingga gcd(ϕ(n),e)=1 & 1<e<ϕ(n):\u001b[0m", end='\n\n')
        
        foundEncryptionKey = False
        while not foundEncryptionKey:
            e = random.randint(2, phi - 1)
            if cryptomath.gcd(e, phi) == 1:
                foundEncryptionKey = True
                    
        print("\u001b[33;1me: \u001b[0m", e, end='\n\n')

        print("\u001b[33;1mMemeriksa apakah gcd(e, ϕ)==1: \u001b[0m")
        print("\u001b[33;1mgcd\u001b[0m(", e, ",", phi, ")", '\n' , "=", "\u001b[33;1m", cryptomath.gcd(e, phi))
        v=False
        if cryptomath.gcd(e, phi)==1:
            v=True
        print("Verification Status: ", v, "\u001b[0m", end='\n\n')
        print("\u001b[35;1m(d) Menghitung d, di mana d adalah inversi dari e Langkaho ϕ(n)\u001b[0m", end='\n\n')
        d = cryptomath.findModInverse(e, phi)
       
        
        print("\u001b[33;1md: \u001b[0m",d, end='\n\n')
        
        print("\u001b[33;1mMemeriksa apakah e*d mod ϕ(n) adalah 1 (yang merupakan kondisi yang diperlukan untuk d menjadi inversi dari e mod ϕ(n)): \u001b[0m")
        print(e, "*", d, "mod", phi,'\n' ,"=", e*d % phi, end='\n')
        v=False
        if (e*d % phi)==1:
            v=True
        print("\u001b[33;1mStatus Verifikasi: \u001b[0m", v, end='\n\n')
        
        print("\u001b[35;1m(e) Dibuat menjadi private: (n,e) dan key private dan key pribadi yang dihitung secara berturut-turut adalah:\u001b[0m", end='\n\n')
        print("\u001b[33;1mkey private (n, e): \u001b[0m", "(",n,", " ,e,")", end='\n\n')
        print("\u001b[33;1mkey Pribadi (n, d):  \u001b[0m", "(",n,", " ,d,")", end='\n\n')
        publicInfo = {"n" : n, "e": e}
        privateInfo = {"n" : n, "d": d}
    
        return[(publicInfo),(privateInfo)]
        
    def getPublicKey(self):
        return self.publicKey
    
    def signMessage(self, message, eligible):
        
        print('\n\n')
        for i in range(100):
            print("-", end="")
        print()    
        for i in range(50):
            print(" ", end="")
        print("\u001b[31mLangkah 3\u001b[37m")
        for i in range(100):
            print("-", end="")
        print('\n\n')   
        
        print("\u001b[32;1m3. Admin  Memberikan Otorisasi Pemilih\u001b[0m", end='\n\n')
        print("\u001b[35;1m(a) Admin  menerima m'\u001b[0m", end='\n\n')
        print("\u001b[35;1m(b) Admin  memverifikasi apakah pemilih memenuhi syarat untuk memberikan suara\u001b[0m", end='\n\n')
        if eligible == "y":
            print("\u001b[35;1m(c) Jika pemilih memenuhi syarat, Admin  menandatangani surat suara: sign = ((blind signature)^d) mod n = ((m* (r^e))^d) mod n = (m^d * r^(ed)) mod n = (m^d * r^1) mod n = (m^d * r) mod n(dengan d adalah key pribadi Admin )\u001b[0m", end='\n\n')
            s= pow(message, self.privateKey['d'], self.publicKey['n']) #important # ERR1
            print("\u001b[33;1mTanda Tangan oleh Admin Tanda Tangan: \u001b[0m", s, end='\n\n')
            print("\u001b[35;1m(d) Mengirimkan s' kembali ke pemilih\u001b[0m", end='\n\n')
            return s
        else:
            return None
        
    def verifyVoter(self, eligible):
        pass
        
 
class Voter:
    
    def __init__(self, n, eligible):
        self.eligible = eligible
        
        print("\u001b[35;1m(d) Menghasilkan r sehingga r adalah bilangan prima relatif terhadap n dan 2<= r <=(n-1)\u001b[0m", end='\n\n')
        foundR = False
        while not foundR:
            self.r = random.randint(2, n - 1)       
            if cryptomath.gcd(self.r, n) == 1:
                print("\u001b[33;1mr: \u001b[0m", self.r, end='\n\n')
                foundR = True
        print("\u001b[33;1mMemeriksa apakah gcd(r, n)==1: \u001b[0m", end='\n\n')
        print("\u001b[33;1mgcd \u001b[0m", "(", self.r, ",", n, ")", '\n' , "=", "\u001b[33;1m", cryptomath.gcd(self.r, n), end='\n\n')
        v=False
        if cryptomath.gcd(self.r, n)==1:
            v=True
        print("Status Verifikasi: ", v, "\u001b[0m", end='\n\n')        
    
    def unwrapSignature(self, signedBlindMessage, n):
        print('\n\n')
        for i in range(100):
            print("-", end="")
        print()    
        for i in range(50):
            print(" ", end="")
        print("\u001b[31mLangkah 4\u001b[37m")
        for i in range(100):
            print("-", end="")
        print('\n\n')
        print("\u001b[32;1m4. Pemilih membuka pembungkusan suara\u001b[0m", end='\n\n')
        print("\u001b[35;1m(a) Menerima s'\u001b[0m", end='\n\n')
        
        print("\u001b[35;1m(g) Menghitung rInv, di mana rInv adalah kebalikan dari r Langkaho n. r akan digunakan oleh pemilih untuk membuka blinded message.\u001b[0m", end='\n\n')
        rInv = cryptomath.findModInverse(self.r, n) # ERR3
        print("rInv: ", rInv)
         
        print()    
        print("\u001b[33;1mMemeriksa apakah r * rInv mod n adalah 1 (yang merupakan kondisi yang dibutuhkan agar rInv menjadi invers dari r mod n): \u001b[0m")
        print(self.r, "*", rInv, "mod", n,'\n' ,"=", self.r*rInv % n, end='\n')
        v=False
        if (self.r*rInv % n)==1:
            v=True
        print("\u001b[33;1mStatus Verifikasi: \u001b[0m", v, end='\n\n')
        print("\u001b[35;1m(b) Menghitung s = (s')(rInv) mod n = (m^d * r)*(rInv) mod n = (m^d * 1) mod n = (m^d) mod n \u001b[0m", end='\n\n')
        s = ((signedBlindMessage * rInv) % n)
        print("\u001b[33;1mPesan yang Ditandatangani, s: \u001b[0m", s, end='\n\n')
        print("\u001b[35;1m(c) Mengirimkan tanda tangan s ke lokasi penerimaan suara \u001b[0m", end='\n\n')
        return s
    
    
    def blindMessage(self, m, n, e):
         print("\u001b[35;1m(e) Menghitung pesan tersembunyi (blinded message): m' = (m* (r^e)) mod n (di mana n dan e diketahui oleh private)u001b[0m", end='\n\n')
         blindMessage = (m * pow(self.r, e, n)) % n  #returns r to the power of e, Langkahus n.
         print("\u001b[33;1mBlinded Message: \u001b[0m", blindMessage)
         return blindMessage
         
    
    def getEligibility(self):
        return self.eligible

    
def verifySignature(message, randNum, signature, publicE, publicN):
    ballot= pow(signature, publicE, publicN) #decrypting, it gets back the message_hash
    verificationStatus = (int(hashlib.sha256((str(message) + str(randNum)).encode('utf-8')).hexdigest(),16) == ballot)
    print("\u001b[35;1mPesan hash terenkripsi/ditandatangani dideskripsi dengan 5 private Admin yang telah menandatanganinya (s^e) mod n = (m^d)^e mod n = (m^1) mod n = m mod n = m : \u001b[0m","\n", ballot, end="\n\n")
    print("\u001b[35;1mHitung hash dari pesan gabungan sebagai hash(pesan gabungan): \n \u001b[0m" ,int(hashlib.sha256((str(message) + str(randNum)).encode('utf-8')).hexdigest(),16), end='\n\n')
    print("\u001b[31mJika kedua nilai di atas sama, maka dapat dipastikan bahwa pesan tersebut memang telah disetujui oleh Admin yang menandatanganinya. \u001b[0m", end='\n\n')
    decoded_message = message
    return verificationStatus, decoded_message   