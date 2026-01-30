#Substitution cipher

import random
import string

ch = " " + string.ascii_letters + string.digits + string.punctuation 
#Generating key
def gen_key():
    
    key = list(ch)
    random.shuffle(key)
    return key

#ENCRYPTION
def encrypt(plain_text, key):
    cipher_text = ""
    for letter in plain_text:
        try:
            index = ch.index(letter)
            cipher_text += key[index]
        except ValueError:
            cipher_text += letter
    return cipher_text

#DECRYPTION
def decrypt(cipher_text, key):
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += ch[index]
    return plain_text

#MAIN
def main():
    key = gen_key()
    plain_text = input("Enter plain text to encrypt :")
    cipher_text = encrypt(plain_text, key)
    print(f"plain text : {plain_text}")
    print(f"cipher text : {cipher_text}")
    print("Encryption Successful !!\n")
    pt = decrypt(cipher_text, key)
    if plain_text == pt:
        print("Decryption Successful !!")
        print(f"cipher text : {cipher_text}")
        print(f"plain text : {plain_text}")

if __name__ == '__main__':
    main()