import rsa_util
from Crypto.Util import number

#this file was created to make the test option for the RSA algorithm
def run_test():
    #ask for the plain message
	testMessage = raw_input("Test case: enter message that you want to encrypt: ")
    #generate public and private key
	rsa_test = rsa_util.RSA(256)
	n = rsa_test.getN()
	phiN = rsa_test.getPhiN()
	public_element_e = rsa_test.select_e(phiN)
	private_element_d = rsa_test.select_d(public_element_e,phiN)
    
    #run the encryption process
	byteMessage = number.bytes_to_long(str.encode(testMessage))
	print('The message has been transformed into binary before Encryption: ')
	print(bin(byteMessage))
	encryptMessage = rsa_test.encrypt_message(byteMessage,public_element_e,n)
	print('This is the ciphertext after the encryption process: ')
	print(bin(encryptMessage))
    
    #run the decryption process
	decryptMessage = rsa_test.decrypt_message(encryptMessage,private_element_d,n)
	print('This is the recover message from decryption: ')
	print(bin(decryptMessage))
	stringDecryptMessage = (number.long_to_bytes(decryptMessage))
    
    #recover the intial plain message
	initialMessage = stringDecryptMessage.decode()
	print('The recover message is : ')
	print(initialMessage)
