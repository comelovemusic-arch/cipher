def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


choice = input("Do you want to encrypt(1) or decrypt a text(2): ")

while True:

    if choice == '1':

        to_encrypt = input("give me words or sentences to encrypt: ")
        encrypt_shift = input("Give an encrypt key 0 - 25.  you must remember the number \n because you canr decrypt with out stating it!")
        encrypt_shift = int(encrypt_shift)

        encrypted_text = encrypt(to_encrypt, encrypt_shift)
        print(encrypted_text)
        break

    elif choice == '2':

        to_decrypt = input("give me words or sentences to decrypt: ")
        decrypt_shift = input("Give me the encrypt key you used: ")
        decrypt_shift = int(decrypt_shift)

        decrypted_text = decrypt(to_decrypt, decrypt_shift)
        print(decrypted_text)
        break

    else:
        choice = input("only enter 1 or 2!!")
