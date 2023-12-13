print("\n**Welcome to encryption genrator**\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encryption(plain_text,no_of_shift):
    encryptedtext =""
    for letter in plain_text:
        postion = alphabet.index(letter)
        new_postion = postion + no_of_shift
        if new_postion > 26 :
           new_postion -=26
        new_letter = alphabet[new_postion]
        encryptedtext += new_letter
    print(f"the encrypted text with shift {no_of_shift} is : {encryptedtext}")   
     
def decryption(plain_text,no_of_shift):
    decryptedtext =""
    for letter in plain_text:
        postion = alphabet.index(letter)
        new_postion = postion - no_of_shift
        if new_postion < 0 :
           new_postion +=26
        new_letter = alphabet[new_postion]
        decryptedtext += new_letter
    print(f"the decrypted text with shift {no_of_shift} is : {decryptedtext}")
number = 0
while number == 0 :
    if direction == "encode":
        encryption(text,shift)
    else:
        decryption(text,shift)
    number = int(input("Enter 0 to continue or 1 to exit\n"))
    if number == 1:
        break    
    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
                
    