


def get_driver_telemetry(session,driver_code:str):
    """
    Get telemetry data (speed, Throttle, Brake, Gear, etc.) for a driver.
    
    """
    laps = session.laps.pick_driver(driver_code).pick_fastest()
    telemetry= laps.get_car_data().add_distance()
    return telemetry