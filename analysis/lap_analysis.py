import pandas as pick_driver

def compare_lap_times(session):

    """
    Return average lap times for each driver
    
    """
    laps=session.laps
    avg_laps= laps.groupby("Driver")["LapTime"].mean().sort_values()
    return avg_laps