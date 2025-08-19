"""FHE Computation Circuit for SecureGenomics Protocol."""

from typing import List
from shared import CryptoContext
import pickle

def compute(encrypted_datasets: List[bytes], public_crypto_context: bytes) -> bytes:
    # Deserialize the public context
    context = CryptoContext.deserialize(public_crypto_context)
    n, _ = context.public_key
    
    encrypted_results = encrypted_datasets[0]
    
    for vector in encrypted_datasets[1:]:
        for i in range(len(encrypted_results)):
            encrypted_results[i] = (encrypted_results[i] * vector[i]) % n**2
            
    return pickle.dumps(encrypted_results)