from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta


KEY = b'kkkkkkkkkkkkkkkk'
FLAG = 'crypto'

def check_admin(cookie, iv):
    print()
    print(f"reveid iv len : {len(iv)}")
    cookie = bytes.fromhex(cookie)
    iv = bytes.fromhex(iv)
    print(f"reveid iv hexa  len : {len(iv)}")

    try:
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(cookie)
        unpadded = unpad(decrypted, 16)
    except ValueError as e:
        return {"error": str(e)}
    print(unpadded)
    print(unpadded.split(b";"))
    if b"admin=True" in unpadded.split(b";"):
        return {"flag": FLAG}
    else:
        return {"error": "Only admin can read the flag"}

def get_cookie():
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    cookie = f"admin=False;expiry={expires_at}".encode()

    iv = os.urandom(16)
    padded = pad(cookie, 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    print(f"iv hexa : {iv.hex()}")
    print(f"enryptted hex : {encrypted.hex()}")
    ciphertext = iv.hex() + encrypted.hex()
    print(f"cookie : {ciphertext}")
    return {"cookie": ciphertext}

print('running ...')
cook = 'be2f364a1b14bfdaf11a36d6896672d5103b5015126f9c6860783c4b8074ca2b4747524cc124b37c365180ad300d8bb5'
print(f"fetched cookies = {cook[32:]}")
print("=================================")
iv = cook[:32]
cookies = cook[32:]
print(f"fetched cookies = {cookies}")
source_iv = bytes.fromhex(iv)
print(f"source iv : {len(source_iv)}")
target = b"admin=True;"
target = pad(target, 16)
print(f"len of target : {len(target)}")
current = b"admin=False;"
current = pad(current, 16)
newiv = bytearray(source_iv)
print(f"before bytearray {len(source_iv)}")
print(len(newiv))
for i in range(len(target)):
	newiv[i] ^= target[i] ^ current[i]

print(f"new iv = {len(newiv)}") 
new_iv = newiv.hex()
print(f"The greatest : {new_iv}")
flag = check_admin(cookies, new_iv)
print(flag)
#   YES !!!!!
#crypto{4u7h3n71c4710n_15_3553n714l}
