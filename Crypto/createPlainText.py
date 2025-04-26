import sys
import os
import base64
import json
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

'''
https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
'''

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Create a plaintext from a ciphertext using AES in CFB mode.")
    parser.add_argument(
        "key",
        type=str,
        help="A cryptographic key in Base64 format"
    )
    parser.add_argument(
        "cipherText",
        type=str,
        help="cipherText and initialization vector (iv) in json format."
    )
    args = parser.parse_args()
    # Decode the key and plaintext from base64 arguments
    key = base64.b64decode(args.key)
    
    input = args.cipherText.split('.')
    #extract cipherText
    cipherText = base64.b64decode(input[0])
    # Initialization vector should be randomly generated and the same length as the key
    iv = base64.b64decode(input[1])

    # Create a cipher object
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    # Create a decryptor object
    decryptor = cipher.decryptor()
    # Decrypt the cipher text
    plaintext = decryptor.update(cipherText) + decryptor.finalize()
    # Output the ciphertext and iv to stdout
    sys.stdout.write(plaintext.decode('ascii'))
    # Return a successful exit status
    sys.exit(1)

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Change to that directory
    os.chdir(script_dir)
    main()