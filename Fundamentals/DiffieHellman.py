from cryptography.hazmat.primitives.asymmetric import dh

parameters = dh.generate_parameters(2, 2048)
server_private_key = parameters.generate_private_key()
server_public_key = server_private_key.public_key()

client_private_key = parameters.generate_private_key()
client_public_key = client_private_key.public_key()

shared_secret1 = server_private_key.exchange(peer_public_key=client_public_key)
shared_secret2 = client_private_key.exchange(peer_public_key=server_public_key)

assert shared_secret1 == shared_secret2, "They are not the same"