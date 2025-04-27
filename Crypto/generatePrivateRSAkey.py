import sys
import os
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Change directory to where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Generate our key
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

pem_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

der_key = key.private_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

# Write our PEM key to disk for safe keeping
with open("privateRSAkey.pem", "wb") as f:
    f.write(pem_key)

#Write the DER key out to the simulation for use on the command line
sys.stdout.write(base64.b64encode(der_key).decode('ascii'))

# Return a successful exit status
sys.exit(1)