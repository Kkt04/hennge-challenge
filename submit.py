import hmac
import hashlib
import struct
import time
import base64
import urllib.request
import urllib.error
import json
import ssl


GITHUB_URL = "https://gist.github.com/YOUR_ACCOUNT/YOUR_GIST_ID"
EMAIL      = "your@email.com"
LANGUAGE   = "python"   


SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE


def hotp(secret_bytes, counter, digits=10):
    """HOTP per RFC 4226 using HMAC-SHA-512."""
    msg = struct.pack('>Q', counter)
    h = hmac.new(secret_bytes, msg, hashlib.sha512).digest()
    offset = h[-1] & 0x0F
    code = struct.unpack('>I', h[offset:offset + 4])[0] & 0x7FFFFFFF
    return str(code % (10 ** digits)).zfill(digits)


def totp(secret_bytes, step=30, digits=10):
    """TOTP per RFC 6238: T0=0, step=30s, HMAC-SHA-512."""
    t = int(time.time()) // step
    return hotp(secret_bytes, t, digits)


def generate_totp_password(email):
    secret_str   = email + "HENNGECHALLENGE004"
    secret_bytes = secret_str.encode('utf-8')
    return totp(secret_bytes)


def submit(github_url, email, language):
    print(f"\n{'='*50}")
    print("HENNGE Challenge - Mission 3 Submission")
    print(f"{'='*50}")
    print(f"  GitHub URL : {github_url}")
    print(f"  Email      : {email}")
    print(f"  Language   : {language}")

    password    = generate_totp_password(email)
    credentials = base64.b64encode(f"{email}:{password}".encode()).decode()
    print(f"  TOTP token : {password}")

    payload = json.dumps({
        "github_url":        github_url,
        "contact_email":     email,
        "solution_language": language
    }).encode('utf-8')

    req = urllib.request.Request(
        "https://api.challenge.hennge.com/challenges/backend-recursion/004",
        data    = payload,
        headers = {
            "Content-Type":  "application/json",
            "Authorization": f"Basic {credentials}"
        },
        method = "POST"
    )

    print(f"\nSending POST request...")
    try:
        with urllib.request.urlopen(req, context=SSL_CTX) as resp:
            body = resp.read().decode()
            print(f"\n✓ SUCCESS! Status: {resp.status}")
            print(f"  Response : {body}")
            print("\nCheck your email — HENNGE will contact you with next steps.")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"\n✗ FAILED. HTTP {e.code}: {body}")
        if e.code == 401:
            print("\nHint: TOTP token expired (valid 30s). Run the script again immediately.")
        elif e.code == 400:
            print("\nHint: Check your GitHub URL and email are correct.")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    submit(GITHUB_URL, EMAIL, LANGUAGE)
