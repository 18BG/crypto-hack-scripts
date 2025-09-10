# import binascii


# with open("cipher.hex") as f:
#     data = f.read().strip()
# print(f"Fetched data : {data}")
# cipher = bytes.fromhex(data)

# blocks = [cipher[i:i+16] for i in range(0, len(cipher), 16)]

# png_header = bytes.fromhex("89504E470D0A1A0A0000000D49484452")

# K = bytes(a ^b for a,b in zip(blocks[0], png_header))

# plaintext = b"".join(
#     bytes(a ^ b for a, b in zip(block, K)) for block in blocks
# )

# with open("recovered.png", "wb") as f:
#     f.write(plaintext)

# print("Image PNG recuperer !")

# recover_png.py
import binascii

# Fichier chiffré exporté depuis l'API ou challenge
ENCRYPTED_FILE = "cipher.hex"
OUTPUT_FILE = "recovered.png"

# En-tête PNG connu (premier bloc de 16 octets + début du chunk IHDR)
PNG_HEADER = bytes.fromhex("89504E470D0A1A0A0000000D49484452")

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """XOR entre deux byte sequences"""
    return bytes([x ^ y for x, y in zip(a, b)])

def main():
    # Lire le fichier chiffré (hexadecimal)
    with open(ENCRYPTED_FILE, "r") as f:
        data = f.read().strip()

    cipher_bytes = bytes.fromhex(data)

    # Couper en blocs de 16 octets
    blocks = [cipher_bytes[i:i+16] for i in range(0, len(cipher_bytes), 16)]

    # Keystream = XOR du premier bloc chiffré avec le header PNG connu
    keystream = xor_bytes(blocks[0], PNG_HEADER)

    # Déchiffrer tous les blocs avec ce même keystream
    plaintext_blocks = [xor_bytes(block, keystream) for block in blocks]

    # Écrire le fichier récupéré
    with open(OUTPUT_FILE, "wb") as f:
        f.write(b"".join(plaintext_blocks))

    print(f"Image PNG récupérée -> {OUTPUT_FILE}")

if __name__ == "__main__":
    main()








