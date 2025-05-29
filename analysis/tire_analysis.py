import pandas as pd 


def get_tire_compound_usage(session):
    """
    Return the tire compound usage for each driver
    """
    tire_data = session.laps[["Driver", "Stint", "Compound", "LapNumber"]]
    tire_summary=(
        tire_data.groupby(["Driver","Stint","Compound"])
        .count()
        .rename(columns={"LapNumber": "Laps"})
        .reset_index()
    )
    return tire_summary