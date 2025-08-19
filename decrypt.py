"""FHE Decryption and Result Interpretation for SecureGenomics Protocol."""

import pickle
from shared import CryptoContext
from typing import Dict, Any

def decrypt_result(encrypted_result: bytes, private_crypto_context: bytes) -> Dict[str, Any]:
    encrypted_result = pickle.loads(encrypted_result)
    private_crypto_context = CryptoContext.deserialize(private_crypto_context)
    
    lambda_, mu = private_crypto_context.private_key
    n, _ = private_crypto_context.public_key
    
    def decrypt_single_value(c: int) -> int:
        l = (pow(c, lambda_, n**2) - 1) // n
        return (l * mu) % n
    
    result = map(decrypt_single_value, encrypted_result)
    return result

def interpret_result(result):
    # remove the extra one at the end to count the number of alleles
    result, num_genomes = result[:-1], result[-1]
    
    print('# Genomes:', num_genomes)
    
    num_alleles = num_genomes * 2
    allele_freqs = [r / num_alleles for r in result]
    
    print('Allele frequencies:', allele_freqs)
    return {
        'allele_frequencies': allele_freqs,
        'num_genomes': num_genomes
    }