import sys
import os
import argparse
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
import base64

# Supported elliptic curves
SUPPORTED_CURVES = {
    "secp256r1": ec.SECP256R1(),
    "secp384r1": ec.SECP384R1(),
    "secp521r1": ec.SECP521R1(),
    # Add more curves here if needed
}

def generate_ecc_private_key(curve_name):
    """
    Generate an ECC private key for the given curve name.
    
    Args:
        curve_name (str): The name of the elliptic curve.
        
    Returns:
        private_key: An ECC private key object.
    """
    curve = SUPPORTED_CURVES.get(curve_name.lower())
    if not curve:
        raise ValueError(f"Unsupported curve: {curve_name}. Supported curves are: {', '.join(SUPPORTED_CURVES.keys())}")
    
    # Generate the private key for the specified curve
    private_key = ec.generate_private_key(curve)
    return private_key

def private_key_to_der(private_key):
    """
    Convert the private key to der format.
    
    Args:
        private_key: The ECC private key object.
        
    Returns:
        str: The der-formatted private key as a string.
    """
    der_data = private_key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return der_data

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate an ECC private key in der format.")
    parser.add_argument(
        "curve",
        type=str,
        default="secp256r1",
        choices=["secp256r1", "secp384r1", "secp521r1"],
        help="The name of the elliptic curve to use (e.g., 'secp256r1')."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="private_key.der",
        help="Optional file to save the private key. If not provided, the key will be printed to stdout."
    )
    args = parser.parse_args()

    # Generate the private key
    private_key = generate_ecc_private_key(args.curve)

    
    # Convert the private key to der format
    der_key = private_key_to_der(private_key)
    sys.stdout.write(base64.b64encode(der_key).decode('ascii'))

    # Output the key to a file or stdout
    if args.output:
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        with open(os.path.join(script_dir,args.output), "wb") as file:
            file.write(der_key)

    sys.exit(1)

if __name__ == "__main__":
    main()
