import secrets
import sympy

from shared import CryptoContext

def generate_keys(bit_length=512):
    p = sympy.nextprime(secrets.randbits(bit_length))
    q = sympy.nextprime(secrets.randbits(bit_length))
    n = p * q
    g = n + 1
    lambda_ = (p - 1) * (q - 1)
    mu = sympy.mod_inverse(lambda_, n)
    
    public_key = (n, g)
    private_key = (lambda_, mu)
    
    public_crypto_context = CryptoContext(
        public_key=public_key,
        private_key=private_key
    )
    private_crypto_context = CryptoContext(
        public_key=None,
        private_key=private_key
    )

    return public_crypto_context.serialize(), private_crypto_context.serialize()