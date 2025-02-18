import sys
import os
import base64
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

'''
https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/
'''

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Create a ciphertext from a plaintext using AES in CFB mode.")
    parser.add_argument(
        "key",
        type=str,
        help="A cryptographic key in Base64 format"
    )
    parser.add_argument(
        "plainText",
        type=str,
        help="plainText in Base64 format"
    )
    args = parser.parse_args()
    # Decode the key and plaintext from base64 arguments
    key = base64.b64decode(args.key)
    plainText = base64.b64decode(args.plainText)

    # Initialization vector should be randomly generated and the same length as the key
    iv = os.urandom(len(key))
    # Create a cipher object
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    # Create an encryptor object
    encryptor = cipher.encryptor()
    # Encrypt the plaintext
    ciphertext = encryptor.update(plainText) + encryptor.finalize()
    # Output the ciphertext and iv to stdout
    sys.stdout.write(
        base64.b64encode(ciphertext).decode('ascii') + 
        "." + 
        base64.b64encode(iv).decode('ascii'))
    # Return a successful exit status
    sys.exit(1)

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Change to that directory
    os.chdir(script_dir)
    main()