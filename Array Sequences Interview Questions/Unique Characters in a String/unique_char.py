def uni_char1(s):
    return len(set(s)) == len(s)

def uni_char(s):

    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)

    return True
