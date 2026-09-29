import hmac
import hashlib

def cracker(hash_string: str, dictionary: dict):
    data = dictionary.get(hash_string)
    if data is not None:
        print(data)
    else:
        print("Hash not found.")



def message_converter():
    data = input("Input the data:")
    sha512_message = hashlib.sha512(data.encode())
    print("Normal:", data)
    print("SHA512:", sha512_message.hexdigest())

def hmac_converter(secret: bytes, data: bytes):
    hmac_object = hmac.new(secret, data, digestmod=hashlib.sha256)
    hex_hmac = hmac_object.hexdigest()

def hmac_signature_verifier(secret: bytes, data: bytes, received_hmac: str):
    hmac_object = hmac.new(secret, data, digestmod=hashlib.sha256)
    if hmac_object.hexdigest() == received_hmac:
        print("Authentic message")
    else:
        print("Not authentic")





message_converter()

