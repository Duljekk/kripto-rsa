import BlindSig as bs
import hashlib
import random
import cryptomath
yell = '\u001b[33;1m'
reset = '\u001b[0m'
red = '\u001b[31m'
pink = '\u001b[35;1m'
              



class poll:
    def __init__(self):
        self.signer = bs.Signer()
        self.publicKey = self.signer.getPublicKey()
        self.n = self.publicKey['n']
        self.e = self.publicKey['e']
        
    def poll_response(self, poll_answer, eligble_answer):
       
       if (eligble_answer == 0):
            eligble_answer = "n"
       elif (eligble_answer == 1):
            eligble_answer = "y"
       
    
       print('\n\n')
       for i in range(100):
            print("-", end="")
       print()    
       for i in range(50):
            print(" ", end="")
       print("\u001b[31mMODUL 2\u001b[37m")
       for i in range(100):
            print("-", end="")
       print('\n\n')    
       print("\u001b[32;1m2. Pemilih Menyiapkan Surat Suara untuk Ditandatangani oleh Otoritas Tertanda:\u001b[0m", end='\n\n')
       print()
       print("\u001b[35;1m(a) Menghasilkan bilangan acak x sehingga 1<=x<=n\u001b[0m", end='\n\n') 
       x = random.randint(1,self.n)
       print("\u001b[33;1mx: \u001b[0m", x, end="\n\n")
    
       print("\u001b[35;1m(b) Pemilih memilih kandidat favorit, opsi, dll. pada surat suara\u001b[0m", end='\n\n')
       message = poll_answer
       print("\u001b[33;1mpoll_answer: \u001b[0m", poll_answer, end="\n\n")
       print("\u001b[35;1m(c) Membuat (menggabungkan) pesan: poll_answer + x dan menghasilkan hashnya\u001b[0m", end='\n\n')
       concat_message = str(message) + str(x)
       print("\u001b[33;1mPesan yang digabungkan: \u001b[0m", concat_message, end="\n\n") 
       message_hash = hashlib.sha256(concat_message.encode('utf-8')).hexdigest()
       message_hash = int(message_hash,16)
       print("\u001b[33;1mhash(Pesan yang digabungkan), m= \u001b[0m", message_hash, end="\n\n")
       voter = bs.Voter(self.n, eligble_answer)
    
       blindMessage = voter.blindMessage(message_hash, self.n, self.e)
       if eligble_answer==1 : 
          print("\u001b[33;1mPesan buta(Blinded message): \u001b[0m" + str(blindMessage))
       print()
       
       print("\u001b[35;1m(f) Mengirimkan m' (blinded message) ke otoritas tertanda\u001b[0m")
       signedBlindMessage = self.signer.signMessage(blindMessage, voter.getEligibility())
 
       if signedBlindMessage == None:
           print("\u001b[31;1mPEMILIH TIDAK MEMENUHI SYARAT....VOTE TIDAK DIIZINKAN!\u001b[0m")
       else:
           print("\u001b[33;1mBlinded message yang ditandatangani: \u001b[0m" + str(signedBlindMessage))
           print()
           signedMessage = voter.unwrapSignature(signedBlindMessage, self.n)
          
           print('\n\n')
           for i in range(100):
              print("-", end="")
           print()    
           for i in range(50):
              print(" ", end="")
            
            
            
           
           print("\u001b[31mMODUL 5\u001b[37m")
           for i in range(100):
              print("-", end="")
           print('\n\n')
            
           print("\u001b[32;1m5. Surat Suara Diterima dan Verifikasi \u001b[0m", end='\n\n')
           print("\u001b[35;1mSuara pemilih dalam surat suara akan terdiri dari hal-hal berikut: \u001b[0m", end='\n\n')
           print("\u001b[33;1m(a) Suara pemilih digabungkan dengan angka x: \u001b[0m",concat_message)
           print()
           print("\u001b[33;1m(b) Hash dari suara pemilih yang digabungkan ditandatangani oleh otoritas, yang pada dasarnya adalah pesan terhash yang dienkripsi dengan kunci privat otoritas tanda tangan (m^d) modulo n: \u001b[0m",signedMessage)
           print()
           verificationStatus, decoded_message = bs.verifySignature(message, x ,signedMessage, self.e, self.n)
           
           print()
           print("\u001b[33;1mStatus verifikasi: \u001b[0m" + str(verificationStatus), end="\n\n")
           if(verificationStatus==True):
               print("\u001b[35;1mKarena verifikasi benar, maka suara adalah digit pertama dari pesan yang digabungkan: \u001b[0m", decoded_message, end='\n\n\n\n')
                
    
       
class poll_machine:
    
    def __init__(self):
        self.p = poll()
        print("\u001b[32;1mMasukkan pilihan Anda\u001b[0m")
        print()
        print("(1) Apel     (2) Mangga      (3) Durian      (4) Nanas    (5) Stroberi")
        poll_=int(input())
        print()
        
        while poll_<1 or poll_>5:
            print("\u001b[31;1mInput",poll_, "bukan opsi yang valid. Silakan masukkan opsi yang valid:\u001b[0m")
            poll_=int(input())
            print()
        print()

        for i in range(100):
            print("-", end="")
        print()    
        for i in range(30):
            print(" ", end="")
        print("\u001b[31m RSA (Rivest–Shamir–Adleman) Encryption \u001b[0m")
        for i in range(100):
            print("-", end="")
        print('\n\n')    


        print("\u001b[35;1m(a)Pilih dua bilangan prima besar p dan q \u001b[0m",  end="\n\n")
        p = cryptomath.findPrime()
        print("\u001b[33;1m p: \u001b[0m", p,  end="\n\n")

        q = cryptomath.findPrime()
        print("\u001b[33;1m q: \u001b[0m", q,  end="\n\n")
        
        print("\u001b[35;1m(b)Hitung n=p*q \u001b[0m",  end="\n\n")
        n = p*q
        print("\u001b[33;1m n: \u001b[0m", n)
        print('\n')

        print("\u001b[35;1m(c)Hitung totien dari n \u001b[0m",  end="\n\n")
        phi = (p - 1)*(q - 1)
        print("\u001b[33;1m ϕ(n): \u001b[0m", phi, end="\n\n")

        print("\u001b[35;1m(d) Pilih public_key sehingga gcd(ϕ(n), public_key)=1 & 1<public_key<ϕ(n):\u001b[0m", end='\n\n')

        foundEncryptionKey = False
        while not foundEncryptionKey:
            public_key = random.randint(2, phi - 1)
            if cryptomath.gcd(public_key, phi) == 1:
                foundEncryptionKey = True
        print("\u001b[33;1me: \u001b[0m", public_key, end='\n\n')

        print("\u001b[35;1m(e) Menghitung private_key, di mana private_key adalah invers dari public_key modulo ϕ(n)\u001b[0m", end='\n\n')
        private_key = cryptomath.findModInverse(public_key, phi)     
        print("\u001b[33;1md: \u001b[0m",private_key, end='\n\n')

        print("\u001b[32;1mMasukkan Nomor NRP: \u001b[0m", end="\n\n")
        while True:
            try:
                idNumber=int(input())
                if len(str(idNumber)) == 10:
                    break
                else:
                    print("Nomor NRP harus memiliki 10 digit. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Masukkan nomor NRP yang valid.")
            
        concat_message = str(idNumber) 
        print("\n\n")

        print("\u001b[35;1m(f) Melakukan hash pada pesan (di sini, pesannya adalah idNumber) \u001b[0m",  end="\n\n")
        idNumber_hash = hashlib.sha256(concat_message.encode('utf-8')).hexdigest()
        idNumber_hash = int(idNumber_hash,16)
        print("\u001b[33;1mHash(idNumber): \u001b[0m", idNumber_hash, end="\n\n")

        print("\u001b[35;1m(g) Pemilih membuat tanda tangan digital menggunakan s=(message_hash)^(private key)modulo n \u001b[0m",  end="\n\n")
        s=pow(idNumber_hash, private_key, n) # ERR2
        print("\u001b[33;1mTanda Tangan Digital, s: \u001b[0m", s, end="\n\n")
        a=0

        ## verification:
        print("\u001b[35;1m(h) Tanda Tangan Digital, s, dan pesan asli, idNumber (tanpa hash) disediakan untuk Verifier \u001b[0m",  end="\n\n")
        print("\u001b[35;1m(i) Verifier menghitung dan membandingkan nilai-nilai \u001b[0m",'\n\n' ,"    1. Pesan yang didekripsi dan", '\n\n' ,"    2. Hash(idNumber)",'\n\n' ,"\u001b[35;1mJika kedua nilai ini sama, maka tanda tangan digital telah terautentikasi \u001b[0m",  end="\n\n")
        concat_message = str(idNumber) 
        print("\u001b[35;1m(j) Hash dari pesan dihitung: \u001b[0m",  end="\n\n")
        verification_hash= hashlib.sha256(concat_message.encode('utf-8')).hexdigest()
        verification_hash = int(verification_hash,16)
        print("\u001b[33;1mHash(idNumber): \u001b[0m", verification_hash, end="\n\n")
        
        print("\u001b[35;1m(k) Mendekripsi pesan(tanpa Hash) menggunakan (tanda_tangan_digital s)^(public key)mod n = (message_hash)^((private key)*(public key))mod n = (message_hash)^1 mod n = (message_hash): \u001b[0m", end='\n\n')
        decrypted_message = pow(s, public_key, n)
        print("\u001b[33;1mPesan yang didekripsi: \u001b[0m", decrypted_message, end="\n\n")
        if decrypted_message == verification_hash:
            a=1

        if a==1:
            print("\u001b[32;1mPemilih Terautentikasi\u001b[0m")
        self.p.poll_response(poll_,a)
    
pm = poll_machine()