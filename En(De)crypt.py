alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(m,s):
    encrypt=""

    for letter in m:
        if letter in alphabet:            
            i=alphabet.index(letter)

            encrypt+=alphabet[(i+shift)%26]

        else:
            encrypt+=letter

    print(f"Here is the text after encryption: {encrypt}")

def decrypt(m,s):
    decrypt=""

    for letter in m:
        if letter in alphabet:
            i=alphabet.index(letter)

            decrypt+=alphabet[(i-shift+26)%26]
        else:
            decrypt+=letter

    print(f"Here is the text after decryption: {decrypt}")

yes='yes'

while yes=='yes':
    case=input("Type 'encrypt' for encryption, type 'decrypt' for decryption!\n").lower()

    message=input("Type your message!\n").lower()

    shift=int(input("Type the shift number!\n"))

    if case=='encrypt':
        encrypt(m=message,s=shift)
    elif case=='decrypt':
        decrypt(m=message,s=shift)

    yes=input("Type 'yes' if you want to go again. Otherwise type 'no'!\n")

print("Goodbye!")