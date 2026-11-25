#!/usr/bin/env python3
"""Chapter 5 Sample Code: Salted PBKDF2-HMAC-SHA512 & Constant-Time Token Check.
Note: In production, prefer Argon2id (e.g., via argon2-cffi) or scrypt where available;
PBKDF2-HMAC-SHA512 with high iterations is used here for Python stdlib portability.
"""

import hashlib
import hmac
import os

ITERATIONS = 210_000  # OWASP minimum baseline for PBKDF2-HMAC-SHA512


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    derived = hashlib.pbkdf2_hmac(
        "sha512",
        password.encode("utf-8"),
        salt,
        ITERATIONS,
        dklen=32,
    )
    return f"pbkdf2_sha512${ITERATIONS}${salt.hex()}${derived.hex()}"


def verify_password(password: str, stored_record: str) -> bool:
    _, iter_str, salt_hex, expected_hex = stored_record.split("$")
    salt = bytes.fromhex(salt_hex)
    expected = bytes.fromhex(expected_hex)
    candidate = hashlib.pbkdf2_hmac(
        "sha512",
        password.encode("utf-8"),
        salt,
        int(iter_str),
        dklen=len(expected),
    )
    return hmac.compare_digest(candidate, expected)


if __name__ == "__main__":
    stored = hash_password("correct horse battery staple")
    print("Stored hash record:", stored)
    print("Valid password check:  ", verify_password("correct horse battery staple", stored))
    print("Invalid password check:", verify_password("wrong password", stored))
