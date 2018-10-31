def original_alphabet():
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    return alphabet


def key():
    user_key = int(input("what should the rotation of the alphabet be (0-25)"))
    return user_key


def user_phrase():
    phrase = input("please type in the phrase you want to encode")
    return phrase

def encode(phrase, alphabet, user_key):
    for user_key in phrase:
        alphabet.index(user_key)
        del alphabet[user_key]



def alphabet(alphabet):
    first = alphabet[::1]
    last = alphabet[::-1]
    new = first + last
    return new


def main():
    original_alphabet()
    user_key = key()
    phrase = user_phrase()
    print(phrase[::-1])


main()
