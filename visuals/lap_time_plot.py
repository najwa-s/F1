import matplotlib.pyplot as plt 


def plot_avg_lap_times(avg_laps):
    """
        Plot average lap times for all drivers.
    """
    plt.figure(figsize=(10, 6))
    avg_laps = avg_laps.dt.total_seconds()
    avg_laps.plot(kind='barh', color='skyblue')
    plt.xlabel("Average Lap Time (s)")
    plt.title("Average Lap Time per Driver")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()