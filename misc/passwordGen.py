import hmac
import hashlib
import time
import base64
import struct


def encode_to_base32(input_string):
    encoded_bytes = base64.b32encode(input_string.encode("utf-8"))
    encoded_string = encoded_bytes.decode("utf-8")
    return encoded_string


# Example usage

secret = "vashishth.amar@gmail.comHENNGECHALLENGE003"
# The shared secret key (base32 encoded)
secret = encode_to_base32(secret)
print(f"secret = {secret}")
# secret = "OZQXG2DJONUHI2BOMFWWC4SAM5WWC2LMFZRW63KIIVHE4R2FINEECTCMIVHEORJQGAZQ===="

# Function to generate TOTP
def generate_totp(secret, interval=30, digits=10, algo=hashlib.sha1):
    # Decode the secret
    key = base64.b32decode(secret, True)

    # Get the current timestamp and calculate the time counter
    counter = int(time.time() / interval)

    # Convert counter to byte array (8-byte)
    counter_bytes = struct.pack(">Q", counter)

    # Generate HMAC hash using the shared secret and the counter
    hmac_hash = hmac.new(key, counter_bytes, algo).digest()

    # Get the offset from the last nibble of the hash
    offset = hmac_hash[-1] & 0x0F

    # Extract 4 bytes starting at the offset
    code = struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF

    # Modulo to get the required number of digits
    otp = code % (10 ** digits)

    # Format the OTP with leading zeros if necessary
    return f'{otp:0{digits}}'


# Generate a 10-digit TOTP password
# Generate the TOTP password based on the user's specified data: Time Step X = 30, T0 = 0, and using HMAC-SHA-512
print(generate_totp(secret, interval=30, digits=10, algo=hashlib.sha512))
