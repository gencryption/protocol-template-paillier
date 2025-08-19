"""
FHE Encryption Module for SecureGenomics Protocol.

This module handles the encryption of encoded genomic data using
the FHE public context for secure computation.
"""

from shared import CryptoContext
import pickle
import secrets
from typing import List

def encrypt_data(encoded_data: List[int], public_crypto_context: bytes) -> bytes:
    public_key = CryptoContext.deserialize(public_crypto_context).public_key
    
    n, g = public_key
    
    def encrypt_single_value(m: int) -> int:
        r = secrets.randint(1, n-1)
        return (pow(g, m, n**2) * pow(r, n, n**2)) % n**2
    
    encrypted_data = map(encrypt_single_value, encoded_data)
    
    encrypted_data_bytes = pickle.dumps(list(encrypted_data))
    
    return encrypted_data_bytes