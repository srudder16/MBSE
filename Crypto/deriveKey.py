import sys
import os
import argparse
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

'''
See https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/
'''

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate a cryptographic key and encode it with base64.")
    parser.add_argument(
        "password",
        type=str,
        help="A user supplied password"
    )
    args = parser.parse_args()

    # Salts should be randomly generated
    salt = os.urandom(16)

    # Save the salt to a file
    with open("salt.bin", "wb") as f:
        f.write(salt)

    # derive key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=16,
        salt=salt,
        iterations=1000
    )
    
    # Derive the key from the password
    key = kdf.derive(args.password.encode())

    # Output the key to stdout
    sys.stdout.write(base64.b64encode(key).decode('ascii'))

    # Return a successful exit status
    sys.exit(1)

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Change to that directory
    os.chdir(script_dir)
    
    main()