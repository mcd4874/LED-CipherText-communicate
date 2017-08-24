#this file contains the RSA algorithm

from Crypto.Util import number




class RSA:
    def __init__(self,bit_length):
        first_prime = number.getPrime(bit_length)
        second_prime = number.getPrime(bit_length)
        self.n = first_prime * second_prime
        self.phiN = (first_prime-1)*(second_prime-1)

    def getN(self):
        return self.n
    def getPhiN(self):
        return self.phiN
    def select_e (self, phiN):
        e = number.getRandomRange(1,phiN)
        while (number.GCD(e,phiN) != 1):
            e = number.getRandomRange(1,phiN)
        return e
    def select_d (self,e, phiN):
        d = number.inverse(e,phiN)
        return d
    
    # modPower to calculate the x^e mod n fast
    def modPower(self, x,e,n):
        if(e == 1):
            return x % n
        else:
            # check if e is divisible by 2
            if (e%2 == 0):
                # run recursive function with e%2
                temp = self.modPower(x, e//2, n)
                # calculate x^2 mod n
                x = (temp**2)%n
            else:
                 # recursive with (e - 1) / 2 for e % 2 != 0
                temp = self.modPower( x, (e-1) // 2, n)
                # calculate ((x^2) mod n) *x mod n
                x = (((temp ** 2) % n) * x) % n
            return x

    # run the encryption algorithm message^e mod n
    def encrypt_message(self,message,e,n):
        return self.modPower(message, e, n)
    # run the decryption algorithm encryptMessage^d mod n
    def decrypt_message(self, encryptMessage, d, n):
        return  self.modPower( encryptMessage, d, n)



