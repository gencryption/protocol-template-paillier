from dataclasses import dataclass
import pickle

@dataclass
class CryptoContext:
    public_key: tuple
    private_key: tuple
    
    def serialize(self) -> bytes:
        return pickle.dumps(self)
    
    @staticmethod
    def deserialize(data: bytes) -> 'CryptoContext':
        return pickle.loads(data)