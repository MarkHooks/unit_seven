def original_alphabet():
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    return alphabet


def key():
    user_key = int(input("what should the rotation of the alphabet be (0-25)"))
    return user_key


def user_encode():
    while True:
        question = input("press e to encode, press d to decode, press q to quit.")
        if question == "e":
            return
        elif question == "d":
            pass
        else:
            break
    return question


def user_phrase():
    phrase = input("please type in the phrase you want to encode")
    phrase.lower()
    phrase = phrase.replace(" ", "")
    return phrase


def new_alphabet(alphabet, user_key):
    first = alphabet[:user_key]
    last = alphabet[user_key:]
    nw_alphabet = last + first
    return nw_alphabet


def encode(phrase, nw_alphabet):
    new_phrase = ""
    for letter in phrase:
        if letter == " ":
            new_phrase = new_phrase + letter
        else:
            index = nw_alphabet.index(letter)
            new_letter = nw_alphabet[index]
            new_phrase = phrase + new_letter
    return new_phrase


def main():
    alphabet = original_alphabet()
    user_phrase()
    user_key = key()
    nw_alphabet = new_alphabet(alphabet, user_key)
    question = input("press e to encode, press d to decode, press q to quit.")
    if question == "e":
        phrase = user_phrase()
        encode(phrase, nw_alphabet)
    elif question == "d":
        pass
    else:
        pass


main()
