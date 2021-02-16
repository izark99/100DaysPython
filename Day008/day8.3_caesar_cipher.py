alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
loop = 'yes'

def encode(message, shift):
    result = ''
    for letter in message:
        index = alphabet.index(letter)
        new_index = index + shift
        if new_index > len(alphabet):
            new_index =  new_index - len(alphabet)
        result += alphabet[new_index]
    print(f"The encode message is {result}")

def decode(message, shift):
    result = ''
    for letter in message:
        index = alphabet.index(letter)
        new_index = index - shift
        if new_index < 0:
            new_index =  len(alphabet) + new_index
        result += alphabet[new_index]
    print(f"The decode message is {result}")

while loop != 'no':
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type shift number:\n"))
    if mode == 'encode':
        encode(message, shift)
        loop = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    elif mode == 'decode':
        decode(message, shift)
        loop = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    