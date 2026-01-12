import hashlib
import base64
import pyotp

raw_secret = b"amarvashishth@hotmail.comHENNGECHALLENGE004"
secret = base64.b32encode(raw_secret).decode()

totp = pyotp.TOTP(
    secret,
    digits=10,
    interval=30,
    digest=hashlib.sha512
)

print(totp.now())
