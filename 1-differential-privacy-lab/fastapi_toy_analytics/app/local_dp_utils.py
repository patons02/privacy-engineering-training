import numpy as np


def randomized_response(value: int, epsilon: float) -> int:
    """
    Applies Randomized Response mechanism for Local Differential Privacy.

    Args:
        value (int): Original binary value (0 or 1).
        epsilon (float): Privacy parameter.

    Returns:
        int: Noised binary value (0 or 1).
    """
    if value not in [0, 1]:
        raise ValueError("Input must be 0 or 1.")

    p = np.exp(epsilon) / (np.exp(epsilon) + 1)

    flip = np.random.rand()

    if flip < p:
        return value
    else:
        return 1 - value
