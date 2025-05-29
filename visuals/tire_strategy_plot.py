import matplotlib.pyplot as plt
import seaborn as sns

def plot_tire_strategy(tire_summary):
    """
    Plot tire usage strategy for each driver.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=tire_summary,
        x="Driver",
        y="Laps",
        hue="Compound"
    )
    plt.title("Tire Compound Usage per Driver")
    plt.ylabel("Number of Laps")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()