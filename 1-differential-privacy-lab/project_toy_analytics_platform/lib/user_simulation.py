import numpy as np

def simulate_user_events(num_users: int = 100) -> dict:
    """
    Simulates fake user events for a toy analytics platform.

    Args:
        num_users (int): Number of users to simulate.

    Returns:
        dict: Dictionary with keys 'clicks', 'pageviews', 'keystrokes' and arrays of 0/1 values.
    """
    np.random.seed(42)  # For reproducibility

    clicks = np.random.binomial(1, 0.6, size=num_users)
    pageviews = np.random.binomial(1, 0.7, size=num_users)
    keystrokes = np.random.binomial(1, 0.5, size=num_users)

    return {
        "clicks": clicks,
        "pageviews": pageviews,
        "keystrokes": keystrokes
    }

