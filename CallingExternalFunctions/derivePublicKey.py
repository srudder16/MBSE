import sys
import os
import argparse
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import base64

def load_private_key_from_der_text(der_text):
    """
    Load an ECC private key from der text.
    
    Args:
        der_text (str): The der-formatted private key as a string.
        
    Returns:
       
     private_key: An ECC private key object.
    """
    
    try:
        
        private_key = serialization.load_der_private_key(
            der_text,
            password=None
        )
        return private_key
    except Exception as e:
        raise ValueError(f"Failed to load private key: {e}")

def get_public_key_der(private_key):
    """
    Generate the public key der from the given private key.
    
    Args:
        private_key: An ECC private key object.
        
    Returns:
        str: The der-formatted public key as a string.
    """
    public_key = private_key.public_key()
    public_der = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return public_der

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate a public key in der format from an ECC private key.")
    parser.add_argument(
        "private_key_text",
        type=str,
        help="The der-formatted ECC private key text (surrounded by quotes)."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="public_key.der",
        help="File to save the public key in DER format."
    )
    args = parser.parse_args()


    # Load the private key
    
    private_der = base64.b64decode(args.private_key_text)
    private_key = load_private_key_from_der_text(private_der)
    
    # Generate the public key in der format
    public_der = get_public_key_der(private_key)
    
    # Output the public key to stdout
    sys.stdout.write(base64.b64encode(public_der).decode('ascii'))

    # Output the key to a file or stdout
    if args.output:
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        with open(os.path.join(script_dir,args.output), "wb") as file:
            file.write(public_der)

    sys.exit(1)

if __name__ == "__main__":
    main()
