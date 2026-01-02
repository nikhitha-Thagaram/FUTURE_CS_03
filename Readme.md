# Secure File Upload System with AES Encryption

This project implements a secure file upload and download web application using Python Flask and AES encryption.

## Features
- Secure file upload and download
- AES encryption for files at rest
- Decryption during file download
- Environment-based encryption key management
- Simple user interface

## Technologies Used
- Python
- Flask
- PyCryptodome
- HTML

## How It Works
1. User uploads a file
2. File is encrypted using AES before storage
3. Encrypted file is saved on the server
4. File is decrypted securely during download

## How to Run
```bash
python app.py
