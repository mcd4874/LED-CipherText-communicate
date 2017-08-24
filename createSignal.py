from sense_hat import SenseHat
import rsa_util
import test_util
import random

from Crypto.Util import number
sense = SenseHat()


#this file would be used to run the main features of the project.

def create_RGB_message():
	message = raw_input("enter message that you want to encrypt: ")
	rsa = rsa_util.RSA(256)
	n = rsa.getN()
	phiN = rsa.getPhiN()
	public_element_e = rsa.select_e(phiN)
	private_element_d = rsa.select_d(public_element_e,phiN)

	byteMessage = number.bytes_to_long(str.encode(message))
	encryptMessage = rsa.encrypt_message(byteMessage,public_element_e,n)

	# divide an encrypted message into 22 slots
	binary = bin(encryptMessage)
	arr = []
	# make sure each slot has 24 bits which represent 3 color red, blue , green
	totalSlots = len(binary)//24
	# there is one remain slot with only 1 red color
	remain = len(binary)-24*totalSlots
	# create a list of 22 slots that each slot contains a 24 bit string that represent one LED on sense hat
	for slot in range (totalSlots):
		currentStart = 2+24*slot
		currentEnd = 2+24*(slot+1)
		arr.append(binary[currentStart:currentEnd])
	arr.append(binary[2+24*totalSlots:len(binary)])

	# transfer each slot in arr into an array of three decimal number that represent red, blue and green
	list_of_RBG = []
	for element in range (len(arr)-1):
		currentRBG = arr[element]
		red = currentRBG[0:8]
		blue = currentRBG[8:16]
		green = currentRBG[16:24]
		RBG = []
		RBG.append(int(red,2))
		RBG.append(int(blue,2))
		RBG.append(int(green,2))
		list_of_RBG.append(RBG)
	# add last element
	list_of_RBG.append([int(arr[21],2),0,0])
	X = [255, 0, 0]  # Red
	O = [255, 255, 255]  # White
	display_RBG= []
	for index in range(len(list_of_RBG)):
		display_RBG.append(list_of_RBG[index])
	for index in range(21):
		display_RBG.append(O)
	for index in range(21):
		display_RBG.append(X)

	random.shuffle(display_RBG)
	sense.set_pixels(display_RBG)

#this loop will run the options for user to pick either test the algorithm or create a ciphertext on the astro pi
while True :
	option = raw_input("Enter 1 to encrypt a message. Enter 2 to run the test ")
	if(len(option) == 1 ):
		if (int(option) == 1):
			create_RGB_message()
		elif (int(option) == 2):
			test_util.run_test()
		else:
			print('you need to either pick option 1 or 2')
	else:
		print('you need to either pick option 1 or 2')

