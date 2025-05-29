from api.session_loader import load_session
from api.telemetry_data import get_driver_telemetry
from api.standings import get_driver_positions

from analysis.lap_analysis import compare_lap_times
from analysis.tire_analysis import get_tire_compound_usage
from analysis.aero_analysis import get_drs_usage

from visuals.lap_time_plot import plot_avg_lap_times
from visuals.telemetry_plot import plot_telemetry
from visuals.tire_strategy_plot import plot_tire_strategy

def main():
    year = 2024
    gp = 'Monza'  # You can change this to any GP name like 'Silverstone'
    session_type = 'R'  # Options: 'FP1', 'Q', 'R', etc.
    driver_code = 'VER'  # 3-letter driver code, e.g., VER, HAM, LEC

    # Load session
    session = load_session(year, gp, session_type)

    # Analysis
    avg_laps = compare_lap_times(session)
    tire_summary = get_tire_compound_usage(session)
    telemetry = get_driver_telemetry(session, driver_code)
    drs_data = get_drs_usage(session, driver_code)

    # Visuals
    plot_avg_lap_times(avg_laps)
    plot_tire_strategy(tire_summary)
    plot_telemetry(telemetry, driver_code)

    # Optional: print DRS zones
    print(f"{driver_code} had DRS active at {len(drs_data)} points.")

if __name__ == "__main__":
    main()