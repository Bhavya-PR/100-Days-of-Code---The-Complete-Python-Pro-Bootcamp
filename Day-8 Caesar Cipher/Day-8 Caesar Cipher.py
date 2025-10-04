import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, directions):
    if directions.lower() == "decode":
        shift_amount *= -1
    elif not directions == "encode" and not directions == "decode":
        print("Please enter a valid direction next time!")
        return
    cipher_text = ""
    for i in range(len(original_text)):
        if original_text[i] in alphabet:
            index_point = (alphabet.index(original_text[i]) + shift_amount)
            cipher_text += alphabet[index_point % 26]
        else:
            cipher_text += original_text[i]
    print(f"Here is the {directions}d result: {cipher_text}")

choice = "yes"
while choice == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, directions=direction)
    choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
