# Security Overview

## Encryption
- AES symmetric encryption is used for all files
- Files are encrypted before being stored on disk
- Decryption happens only during download

## Key Management
- Encryption key is stored using environment variables
- The `.env` file is excluded from version control
- Keys are never hardcoded in the source code

## Data Protection
- Encrypted files are unreadable without the secret key
- Prevents unauthorized access to stored files