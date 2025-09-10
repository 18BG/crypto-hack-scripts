from base64 import *

hexstring = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

byts = bytes.fromhex(hexstring)
print(byts)
b64 = b64encode(byts)
print(b64)
print("\nHere is your flag:")
print(b64.decode('utf-8'))