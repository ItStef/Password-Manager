from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def get_key():
    key = get_random_bytes(32)  # 256-bit key
    if len(key) != 32:
        raise ValueError("Key is not 32 bytes")
    return key
#key = get_key()
Block_Size = 16


def encrypt(password,key, block_size=Block_Size):
    iv = get_random_bytes(block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(password.encode(), block_size))
    cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)
    print(ciphertext)
    print(cipher.iv)
    print(key)
    #decrything ciphertext and printing it  to see if it works
    print(unpad(cipher_decrypt.decrypt(ciphertext), block_size).decode())

    return cipher.iv + ciphertext


def decrypt(ciphertext, key, block_size=Block_Size):
    '''
    try:
        iv = ciphertext[:Block_Size]
        if len(ciphertext) < Block_Size:
            return "Invalid iv length"
        ciphertext = ciphertext[Block_Size:]
        if len(ciphertext) % Block_Size != 0:
            return "Invalid ciphertext length"
    except ValueError:
        return "Invalid values in ciphertext or iv"    
    '''
    iv = ciphertext[:Block_Size]
    ciphertext = ciphertext[Block_Size:]
    print(ciphertext)
    print(iv)
    print(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        plaintext = unpad(cipher.decrypt(ciphertext), Block_Size)
    except ValueError:
        return "Invalid password"
    return plaintext.decode()

