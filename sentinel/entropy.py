import math
from collections import Counter

def calculate_shannon_entropy(data: str) -> float:
    if not data:
        return 0.0
    entropy = 0.0
    length = len(data)
    counts = Counter(data)
    for count in counts.values():
        p_x = count / length
        entropy += - p_x * math.log2(p_x)
    return entropy

def is_high_entropy_secret(token: str, threshold: float = 3.8) -> bool:
    if len(token) < 16:
        return False
    return calculate_shannon_entropy(token) >= threshold
