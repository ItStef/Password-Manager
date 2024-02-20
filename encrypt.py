from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def get_key():
    key = get_random_bytes(32)  # 256-bit key
    if len(key) != 32:
        raise ValueError("Key is not 32 bytes")
    return key

Block_Size = 16

#algorith that turns a string into a master key for future encryption
def generate_master_key(password):
    salt = get_random_bytes(16)
    key = password.encode() + salt
    for i in range(100000):
        key = key + password.encode() + salt
    return key[:32]

def generate_password_zero(key, block_size=Block_Size):
    try:
        iv = get_random_bytes(block_size)
    except ValueError:  
        return "Invalid iv length"
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(key.encode(), block_size))

    password_zero = iv + ciphertext
    with open("password_zero.txt", "wb") as file:
        file.write(password_zero)


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
        if len(iv) < Block_Size:
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

