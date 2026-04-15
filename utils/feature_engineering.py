def extract_features(attempt):
    """
    attempt = {
        "failed_attempts": int,
        "time_interval": float,
        "ip_requests": int
    }
    """
    return [
        attempt["failed_attempts"],
        attempt["time_interval"],
        attempt["ip_requests"]
    ]
