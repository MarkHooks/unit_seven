# Mark Hooks 11/2/18
# this program is to encode and decode a phrase given by the user.


def original_alphabet():
    """
    this is to create an alphabet
    :return: this returns the function
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet


def key():
    """
    this gets the key from the user
    :return: this returns the function
    """
    user_key = int(input("what should the rotation of the alphabet be (0-25) "))
    return user_key


def user_encode():
    """
    this asks if the user wants to encode a phrase or decode a phrase
    :return: this returns the function
    """
    while True:
        question = input("press e to encode, press d to decode, press q to quit. ")
        if question == "e":
            return
        elif question == "d":
            pass
        else:
            break
    return question


def user_phrase():
    """
    this gets the user's phrase
    :return: this returns the function
    """
    phrase = input("please type in the phrase you want to encode/decode.")
    phrase = phrase.lower()
    return phrase


def new_alphabet(alphabet, user_key):
    """
    this is to create a new alphabet based on the key
    :param alphabet: this is the original alphabet
    :param user_key: this is the key that is given by the user
    :return: this returns the function
    """
    first = alphabet[:user_key]
    last = alphabet[user_key:]
    nw_alphabet = last + first
    return nw_alphabet


def encode(phrase, nw_alphabet, alphabet):
    """
    this is to encode the user's phrase
    :param phrase: this is the original phrase
    :param nw_alphabet: this is the new alphabet based on the user's key
    :param alphabet: this is the original alphabet
    :return: this returns the function
    """
    new_phrase = ""
    for letter in phrase:
        if letter not in alphabet:
            new_phrase = new_phrase + letter
        else:
            index = alphabet.index(letter)
            new_letter = nw_alphabet[index]
            new_phrase = new_phrase + new_letter
    return new_phrase


def decode(phrase, nw_alphabet, alphabet):
    """
    this is to decode the user's phrase
    :param phrase: this is the user's phrase
    :param nw_alphabet: this is the new alphabet based on the user's key
    :param alphabet: this is the original alphabet
    :return: this returns the function
    """
    nw_phrase = ""
    for letter in phrase:
        if letter not in nw_alphabet:
            nw_phrase = nw_phrase + letter
        else:
            index = nw_alphabet.index(letter)
            new_letter = alphabet[index]
            nw_phrase = nw_phrase + new_letter
    return nw_phrase


def main():
    question = input("press e to encode, press d to decode, press q to quit:")
    if question == "e":
        # this encodes the phrase
        alphabet = original_alphabet()
        user_key = key()
        nw_alphabet = new_alphabet(alphabet, user_key)
        phrase = user_phrase()
        new_phrase = encode(phrase, nw_alphabet, alphabet)
        print(new_phrase)
    elif question == "d":
        # this decodes the phrase
        alphabet = original_alphabet()
        user_key = key()
        nw_alphabet = new_alphabet(alphabet, user_key)
        phrase = user_phrase()
        nw_phrase = decode(phrase, nw_alphabet, alphabet)
        print(nw_phrase)
    elif question == "q":
        print("thanks for playing")
    else:
        pass


main()
