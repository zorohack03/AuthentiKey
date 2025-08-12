# Digital Signature Creator

## Project Description

Digital Signature Creator is a Python-based project that generates public and private keys, and creates digital signatures for a given message using RSA cryptography. This project is designed to demonstrate the fundamental principles of digital signatures and public key cryptography.

## Features

- **RSA Key Generation**: Generates a pair of RSA keys (public and private) with 512-bit prime numbers.
- **Digital Signature Creation**: Signs a user-provided message using the RSA private key and SHA-256 hashing algorithm.
- **Base64 Encoding**: Encodes the generated digital signature in Base64 format for easy readability and transmission.
- **Key Export**: Exports the public and private keys in PEM format.

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/zorohack03/AuthentiKey.git
    cd AuthentiKey
    ```

2. **Install Dependencies**:
    Ensure you have `pycryptodome` installed:
    ```bash
    pip install pycryptodome
    ```

3. **Run the Script**:
    ```bash
    python digital_signature_creator.py
    ```

4. **Enter Your Message**:
    When prompted, enter the message you want to sign.



## How It Works

1. **Prime Number Generation**: Generates two large prime numbers (512 bits each).
2. **Compute `n` and `φ(n)`**: Computes the modulus `n` and the totient `φ(n)`.
3. **Public Exponent Selection**: Chooses a public exponent `e` that is coprime with `φ(n)`.
4. **Private Exponent Calculation**: Calculates the private exponent `d` using the modular inverse of `e`.
5. **RSA Key Construction**: Constructs the RSA public and private keys using the calculated values.
6. **Message Hashing**: Hashes the input message using SHA-256.
7. **Digital Signature**: Signs the hashed message with the RSA private key.
8. **Base64 Encoding**: Encodes the digital signature in Base64 format.
9. **Key Export**: Exports the RSA public and private keys in PEM format.

