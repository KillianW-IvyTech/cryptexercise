from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Symmetric encryption (Fernet / AES-128-CBC)
def symmetric_demo(message: str):
    print("=== Symmetric (Fernet) ===")

    # Generate secret key, anyone can decrypt
    key = Fernet.generate_key()
    f = Fernet(key)

    ciphertext = f.encrypt(message.encode())
    print(f"Encrypted : {ciphertext}")

    plaintext = f.decrypt(ciphertext).decode()
    print(f"Decrypted : {plaintext}")


# Asymmetric encryption (RSA)

def asymmetric_demo(message: str):
    print("\n=== Asymmetric (RSA) ===")

    # Generate key pair
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Encrypt with public key
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    print(f"Encrypted : {ciphertext.hex()[:60]}...")

    # Decrypt with private key
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    ).decode()
    print(f"Decrypted : {plaintext}")


if __name__ == "__main__":
    msg = "You can see me WAIT OH NOOOOO"
    symmetric_demo(msg)
    asymmetric_demo(msg)
