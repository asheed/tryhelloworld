def encrypt(raw, shift):
    ret = ''
    for char in raw:
        ret += chr(ord(char) + shift)
    return ret

def decrypt(raw, shift):
    ret = ''
    for char in raw:
        ret += chr(ord(char) - shift)
    return ret

if __name__ == "__main__":
    raw = input("input string : ")
    shift = int(input("shift : "))
    encrypted = encrypt(raw, shift)
    print("encrypted : " + encrypted)

    decrypted = decrypt(encrypted, shift)
    print("decrypted : " + decrypted)