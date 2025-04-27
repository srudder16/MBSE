import sys
import os
import base64
import argparse
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate a cryptographic key and encode it with base64.")
    parser.add_argument(
        "private",
        type=str,
        help="An Base64-encoded RSA Key in DER format."
    )
    args = parser.parse_args()

    private_der = base64.b64decode(args.private)
    
    private_key = serialization.load_der_private_key( private_der,password=None)
    
    public_key = private_key.public_key()

    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    # Output the key to stdout
    sys.stdout.write(base64.b64encode(public_key_bytes).decode('ascii'))
    
    public_pem_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # Write our public PEM key to disk for safe keeping
    with open("publicRSAkey.pem", "wb") as f:
        f.write(public_pem_key)

    # Return a successful exit status
    sys.exit(1)

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Change to that directory
    os.chdir(script_dir)
    
    main()