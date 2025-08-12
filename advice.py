def get_advice(bs):
    if bs < 70:
        return "Low blood sugar detected. Consume fast-acting carbohydrates such as glucose tablets or fruit juice immediately."
    elif bs > 180:
        return "High blood sugar detected. Consider insulin administration, light exercise, or consulting a healthcare provider."
    else:
        return "Blood sugar is within the normal range. Continue monitoring and maintain balanced meals and activity."
