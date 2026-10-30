import jwt

payload = {"username": "admin"}
secret = "secret" # weak secret key
encoded_jwt = jwt.encode(payload, secret, algorithm="HS256")
print(encoded_jwt)

"""secret = "fakesecret"
decoded_jwt = jwt.decode(encoded_jwt, secret, algorithms="HS256")
print(decoded_jwt)"""