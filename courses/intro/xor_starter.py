#xor0

#def xor13():
#     word = "label"
#     key = 13
#     result = []
#     for char in word:
#         result.append(chr(ord(char) ^ key))
#     return ''.join(result)
# print(xor13())

#xor1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"

# #KEY2 ^ KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
# ANS1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
# #KEY2 = KEY1 ^ ANS1

# KEY2 = bytes(k1 ^ a1 for k1, a1 in zip(bytes.fromhex(KEY1), bytes.fromhex(ANS1)))

# #KEY2 ^ KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
# ANS2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
# #KEY3 = KEY2 ^ ANS2
# KEY3 = bytes(k2 ^ a2 for k2, a2 in zip(KEY2, bytes.fromhex(ANS2)))

# #FLAG ^ KEY1 ^ KEY3 ^ KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
# ANS3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# # FLAG ^ KEY1 ^ KEY3 ^ KEY2 = Q
# # FLAG = Q ^ KEY1 ^ KEY3 ^ KEY2

# def get_flag():
#     Q = bytes.fromhex(ANS3)
#     flag = bytes(q ^ k1 ^ k3 ^ k2 for q, k1, k3, k2 in zip(Q, bytes.fromhex(KEY1), KEY3, KEY2))
#     return flag.decode()
# print(get_flag())




# #xoreKey0 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# hexs = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# suposed_start = b'crypto{'

# hexb = bytes.fromhex(hexs)


# res = bytes([h ^ s for h, s in zip(hexb, suposed_start)])
# r1 = res[1]

# for hx in hexb:
#     print(chr(hx ^ r1), end='')
# print()







# from binascii import unhexlify

# def guess_single_byte_xor_key(cipher_hex, known_start):
#     cipher_bytes = unhexlify(cipher_hex)
#     known_bytes = known_start.encode()

#     # Essayer de déduire la clé à partir des premiers octets connus
#     possible_keys = [c ^ k for c, k in zip(cipher_bytes[:len(known_bytes)], known_bytes)]

#     # Vérifier que toutes les clés déduites sont identiques
#     if all(k == possible_keys[0] for k in possible_keys):
#         key = possible_keys[0]
#         print(f"[+] Clé XOR déduite : {hex(key)}")
        
#         # Déchiffrer tout le message avec cette clé
#         decrypted = bytes([b ^ key for b in cipher_bytes])
#         try:
#             print(f"[+] Message déchiffré : {decrypted.decode()}")
#         except UnicodeDecodeError:
#             print("[!] Impossible de décoder le message en UTF-8.")
#         return decrypted
#     else:
#         print("[!] Les octets initiaux ne révèlent pas une clé unique.")
#         print(f"[Debug] Clés trouvées : {possible_keys}")
#         return None


# # Exemple d'utilisation :
# cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
# known_start = "crypto{"  # Ce qu'on suppose au début du message

# guess_single_byte_xor_key(cipher_hex, known_start)

#xorKey1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

cipher_byt = bytes.fromhex(cipher_hex)

known_start = b'myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey'

## xore_key = bytes([c ^ k for c, k in zip(cipher_byt[:len(known_start)], known_start)])
xore_key = bytes([c ^ k for c, k in zip(cipher_byt[:len(known_start)], known_start)])

print(f"[+] Clé XOR déduite : {xore_key}")

