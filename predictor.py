from scipy.stats import linregress
import numpy as np
import pandas as pd
import utils
import circadian

def predict_next(data):
    if len(data) < 2:
        return "Insufficient data for prediction."
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['time_num'] = (data['timestamp'] - data['timestamp'].min()).dt.total_seconds() / 3600.0  # In hours for better scaling
    x = data['time_num'].values
    y = data['blood_sugar'].values
    slope, intercept, _, _, _ = linregress(x, y)
    next_time = data['time_num'].max() + 1  # 1 hour later
    predicted = slope * next_time + intercept
    current_time = utils.get_current_timestamp()
    factor = circadian.circadian_factor(current_time)
    predicted *= factor
    return f"Predicted blood sugar in 1 hour: {predicted:.2f} mg/dL (adjusted for circadian rhythm)."
