import matplotlib.pyplot as plt

def plot_telemetry(telemetry, driver_code: str):
    """
    Plot telemetry data (Speed, Throttle, Brake) over distance.
    """
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(telemetry['Distance'], telemetry['Speed'], label='Speed (km/h)', color='red')
    ax1.set_ylabel('Speed (km/h)', color='red')
    ax1.set_xlabel('Distance (m)')
    
    ax2 = ax1.twinx()
    ax2.plot(telemetry['Distance'], telemetry['Throttle'], label='Throttle', color='green', alpha=0.6)
    ax2.plot(telemetry['Distance'], telemetry['Brake'], label='Brake', color='blue', alpha=0.6)
    ax2.set_ylabel('Throttle / Brake')
    
    plt.title(f"{driver_code} - Telemetry Data")
    fig.legend(loc='upper right')
    plt.tight_layout()
    plt.show()