

def get_drs_usage(session,driver_code:str):
    """
        Return DRS usage data (where DRS was active) for a driver.

    """  
    laps=session.laps.pick_driver(driver_code).pick_fastest()
    telemetry=laps.get_car_data().add_distance()
    drs_data=telemetry[telemetry["DRS"]==1]
    return drs_data