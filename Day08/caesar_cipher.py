
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end_encryption = False
while not end_encryption:
    def caesar(text, shift, direction):
        result = ""
        if direction == "encode":
            for i in text:
                result += alphabet[alphabet.index(i) + shift]
            print(f"{direction} Cipher Text {result}")
        elif direction == "decode":
            for i in text:
                result += alphabet[alphabet.index(i) - shift]
            print(f"{direction} Cipher Text {result}")
        else:
            print("Invalid Options")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    # print(shift)
    caesar(text=text, shift=shift, direction=direction)
    user = input("do you want to perform again Yes or No : ").lower()
    if user == "no":
        end_encryption = True
        print("Exiting......")
