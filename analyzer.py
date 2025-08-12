import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import tkinter as tk

def plot_trends(data, master):
    if data.empty:
        return None
    fig, ax = plt.subplots(figsize=(6, 4))
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    ax.plot(data['timestamp'], data['blood_sugar'], marker='o', linestyle='-')
    ax.set_xlabel('Time')
    ax.set_ylabel('Blood Sugar (mg/dL)')
    ax.set_title('Blood Sugar Trends')
    canvas = FigureCanvasTkAgg(fig, master=master)
    return canvas

def get_stats(data):
    if data.empty:
        return "No data available."
    stats = data['blood_sugar'].describe()
    return stats.to_string()
