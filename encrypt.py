from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def get_key():
    key = get_random_bytes(32)  # 256-bit key
    if len(key) != 32:
        raise ValueError("Key is not 32 bytes")
    return key

Block_Size = 16

#password encryption
def encrypt(password,key, block_size=Block_Size):
    try:
        iv = get_random_bytes(block_size)
    except ValueError:  
        return "Invalid iv length"
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(password.encode(), block_size))

    return cipher.iv + ciphertext

#password decryption
def decrypt(ciphertext, key, block_size=Block_Size):
    try:
        iv = ciphertext[:Block_Size]
        if len(ciphertext) < Block_Size:
            return "Invalid iv length"
        ciphertext = ciphertext[Block_Size:]
        if len(ciphertext) % Block_Size != 0:
            return "Invalid ciphertext length"
    except ValueError:
        return "Invalid values in ciphertext or iv"    
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        plaintext = unpad(cipher.decrypt(ciphertext), Block_Size)
    except ValueError:
        return "Invalid password"
    return plaintext.decode()

