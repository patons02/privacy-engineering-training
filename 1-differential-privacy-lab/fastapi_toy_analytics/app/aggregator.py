class Aggregator:
    def __init__(self):
        self.event_counts = {}
        self.num_users = 0  # Total users who registered

    def add_event(self, event_type: str, noised_value: int):
        """
        Adds a noised event value to the aggregator.
        """
        if event_type not in self.event_counts:
            self.event_counts[event_type] = 0
        self.event_counts[event_type] += noised_value

    def estimate_counts(self, num_users: int, epsilon: float) -> dict:
        """
        Estimates true counts based on Randomized Response.

        Args:
            num_users (int): Total number of users
            epsilon (float): Privacy parameter

        Returns:
            dict: Estimated true counts
        """
        if num_users == 0:
            return {event: 0 for event in self.event_counts}

        est = {}
        p = np.exp(epsilon) / (np.exp(epsilon) + 1)

        for event_type, noised_sum in self.event_counts.items():
            est_count = (noised_sum - (1 - p) * num_users) / (2 * p - 1)
            est[event_type] = max(
                0, min(num_users, est_count)
            )  # Clamp between 0 and num_users
        return est
