alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("Cesarova šifra")

def code_messege (messege, function, shift):
    text_message = " "
    for one_letter in messege:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            if function == "encode":
                new_index = index + shift
                text_message += alphabet[new_index]
            if function == "decode":
                new_index = index - shift
                text_message += alphabet [new_index]
    print(f" Vaše zpráva byla {function} a zní {text_message}")


lets_continue = "ano"

while lets_continue == "ano":
    message = input("Zadejte zprávu: ")
    function = input("Zadejte encode/decode: ")
    shift = int(input("zadejte číslo kodu: "))
    code_messege(message, function, shift)
    lets_continue = input("chcete pokračovat? Ano/Ne ").lower()