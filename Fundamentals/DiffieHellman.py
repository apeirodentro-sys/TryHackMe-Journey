from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
import cryptography.exceptions

class client:
    def __init__(self, rsa_public_key: rsa.RSAPublicKey):
        self.rsa_public_key = rsa_public_key
    def verify(self, signature: bytes, message: bytes):
        try:
            self.rsa_public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.DIGEST_LENGTH,
                ),
                algorithm=hashes.SHA256(),
            )
            print("Valid signature: the message and signer are authentic.")
        except InvalidSignature:
            print("Invalid Signature")
            

class server:
    def __init__(self):
        self.rsa_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.rsa_public_key = self.rsa_private_key.public_key()
        self.message = b"I am who I am"
    def sign(self):
        signature = self.rsa_private_key.sign(
            self.message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.DIGEST_LENGTH,
            ),
            algorithm=hashes.SHA256(),
            )
        return signature


server1 = server()
signature = server1.sign()


client1 = client(server1.rsa_public_key)
client1.verify(signature, server1.message)





parameters = dh.generate_parameters(2, 2048)
server_private_key = parameters.generate_private_key()
server_public_key = server_private_key.public_key()

client_private_key = parameters.generate_private_key()
client_public_key = client_private_key.public_key()

shared_secret1 = server_private_key.exchange(peer_public_key=client_public_key)
shared_secret2 = client_private_key.exchange(peer_public_key=server_public_key)

assert shared_secret1 == shared_secret2, "They are not the same"