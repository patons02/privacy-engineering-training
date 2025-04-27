import numpy as np

def aggregate_noised_data(noised_data: dict) -> dict:
    """
    Aggregates noised user event data.

    Args:
        noised_data (dict): Dictionary of noised arrays.

    Returns:
        dict: Sum of events for each category.
    """
    summary = {}
    for event_type, values in noised_data.items():
        summary[event_type] = np.sum(values)
    return summary

def estimate_true_counts(aggregated_noised: dict, num_users: int, epsilon: float) -> dict:
    """
    Estimates true counts from noised aggregates using Randomized Response formulas.

    Args:
        aggregated_noised (dict): Aggregated noised sums.
        num_users (int): Total number of users.
        epsilon (float): Privacy parameter.

    Returns:
        dict: Estimated true counts for each event type.
    """
    est = {}
    p = np.exp(epsilon) / (np.exp(epsilon) + 1)
    for event_type, noised_sum in aggregated_noised.items():
        est_count = (noised_sum - (1 - p) * num_users) / (2 * p - 1)
        est[event_type] = max(0, min(num_users, est_count))  # Clamp between 0 and num_users
    return est

