import math

class EntropyScanner:
    """Calculates Shannon entropy to identify high-entropy tokens and API secrets."""
    @staticmethod
    def shannon_entropy(data: str) -> float:
        if not data:
            return 0.0
        entropy = 0.0
        length = len(data)
        freq = {char: data.count(char) for char in set(data)}
        for count in freq.values():
            p = count / length
            entropy -= p * math.log2(p)
        return round(entropy, 3)

    @classmethod
    def is_likely_secret(cls, token: str, threshold: float = 3.8) -> bool:
        if len(token) < 16:
            return False
        return cls.shannon_entropy(token) >= threshold
