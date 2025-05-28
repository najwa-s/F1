

def get_driver_positions(session):
    """
        Get drivers positions over the laps.
    """
    return session.lap[["Driver","LapNumber","Position"]]