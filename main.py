def input_choice():
    while True:
        choice = input('Deseja encriptar (E) ou descriptar (D) a mensagem? ').upper()
        if choice in ('E', 'D'):
            return choice
        else:
            print("Escolha inválida. Por favor, escolha 'E' para encriptar ou 'D' para descriptar.")

def input_text_and_key():
    text = input('Mensagem: ')
    custom_key = input('Key: ')
    return text, custom_key

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

choice = input_choice()
text, custom_key = input_text_and_key()

if choice == 'E':
    result = encrypt(text, custom_key)
    print(f'\nTexto encriptado: {result}\n')
elif choice == 'D':
    result = decrypt(text, custom_key)
    print(f'\nTexto desencriptado: {result}\n')