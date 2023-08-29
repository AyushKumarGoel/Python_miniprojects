from art import logo
print(logo)
print("Welcome to Caesar Ciper\n")
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def ciper():
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    ciper_direc = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    a = ""
    for i in text:
        position = letters.index(i)
        if ciper_direc == "encode":
            new_position = letters.index(i) + shift
        elif ciper_direc == "decode":
            new_position = letters.index(i) - shift
        a += letters[new_position]
    print(a)
    Q=input("Do you want to continue(y/n)")
    if(Q=='y'):
        ciper()
    else:
        print("Goodbye")
        return

ciper()