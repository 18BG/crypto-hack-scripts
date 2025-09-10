from Crypto.Util.Padding import pad


iv = 'fbfa4970824b1fb280d6c896422f6891'
source_iv = bytes.fromhex(iv)
source_iv = pad(source_iv, 16)
print(source_iv)

target = b"admin=True"
target = pad(target, 16)

current = b"admin=false"
current = pad(current, 16)
newiv = bytearray(source_iv)
for i in range(len(target)):
	newiv[i] ^= target[i] ^ current[i]

print(f"new iv = {source_iv.hex()}") 
