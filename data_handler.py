import pandas as pd
import os

LOG_FILE = 'datasets/user_logs.csv'
FOOD_FILE = 'datasets/foods.csv'

def load_foods():
    if not os.path.exists(FOOD_FILE):
        data = {
            'food': ['Apple', 'Banana', 'Rice', 'Chicken', 'Salad', 'Bread', 'Yogurt', 'Pasta', 'Fish', 'Orange', 'Potato', 'Eggs', 'Cheese', 'Nuts', 'Carrot'],
            'gi': [39, 62, 73, 0, 15, 71, 35, 50, 0, 40, 85, 0, 0, 15, 35],
            'carbs_per_100g': [14, 23, 28, 0, 5, 50, 5, 25, 0, 12, 20, 1, 1, 20, 8]
        }
        df = pd.DataFrame(data)
        df.to_csv(FOOD_FILE, index=False)
    return pd.read_csv(FOOD_FILE)

def load_logs():
    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame(columns=['timestamp', 'blood_sugar', 'meal', 'exercise', 'notes', 'glycemic_load'])
        df.to_csv(LOG_FILE, index=False)
    return pd.read_csv(LOG_FILE)

def save_log(entry):
    df = load_logs()
    foods = load_foods()
    meal = entry.get('meal', '')
    if meal:
        food_row = foods[foods['food'] == meal]
        if not food_row.empty:
            gi = food_row['gi'].values[0]
            carbs = food_row['carbs_per_100g'].values[0]
            entry['glycemic_load'] = (gi * carbs) / 100
        else:
            entry['glycemic_load'] = 0
    else:
        entry['glycemic_load'] = 0
    new_df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    new_df.to_csv(LOG_FILE, index=False)
