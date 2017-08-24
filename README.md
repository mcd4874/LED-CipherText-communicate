# LED-CipherText-communicate
he ultimate goal of the project is two devices can communciate secret message through color

Part1:
transform a piece of text onto an 8x8 LED RBG signal on a raspberry PI sense hat 

The RSA encryption will be applied onto the text and the ciphertext will be transformed into 64 slots where each slot represent a color on the Astro Pi.
The Astro Pi will display the color to represent the encrypted message. 


Run the createSignal.py to test the code. 
This project require a raspberry Pi and an Astro Pi sense Hat to run. 

Part2:
Apply the RSA decryption algorithm to decrypt the signal from part 1 to obtain the initial message. 
