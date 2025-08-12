# GlucoTrack: Diabetes Management Assistant

## Description

GlucoTrack is a comprehensive Python application designed to assist individuals in managing diabetes through tracking, analysis, and prediction of blood sugar levels. It allows users to log readings along with meals and exercises, view historical data with statistical summaries and visualizations, predict future blood sugar trends using linear regression, and receive advisory messages based on scientific guidelines. The application integrates concepts from nutrition science (glycemic index and load calculations), chronobiology (circadian rhythm adjustments to predictions), and basic statistics to provide a holistic tool.

This project showcases advanced Python development skills, including modular architecture, object-oriented programming, data manipulation, graphical user interfaces, and error handling. It is intended for educational and demonstrative purposes and should not replace professional medical advice.

## Folder Structure

            GlucoTrack/
            ├── datasets/
            │   ├── foods.csv
            ├── README.md
            ├── advice.py
            ├── analyzer.py
            ├── circadian.py
            ├── data_handler.py
            ├── main.py
            ├── predictor.py
            ├── ui.py
            └── utils.py

## Features

- User-friendly GUI with tabbed navigation for logging entries, viewing data, making predictions, and getting advice.
- Data logging with validation for blood sugar readings, meals (from a preloaded food database with GI and carbs), exercises, and notes.
- Visualization of blood sugar trends using line plots embedded in the interface.
- Statistical summaries of historical data (e.g., mean, min, max).
- Prediction of next-hour blood sugar levels via linear regression, adjusted for circadian factors.
- Advisory system based on blood sugar thresholds, drawing from general diabetes management principles.
- Persistent data storage in CSV format for logs and a predefined food database.
- Broad scientific integration: Incorporates glycemic load estimation during logging, time-series analysis, and circadian rhythm effects on metabolism (e.g., slight adjustments during night hours based on research indicating varied insulin sensitivity).

## Requirements

- Python 3.8 or higher.
- Libraries: pandas, numpy, scipy, matplotlib (install via `pip install pandas numpy scipy matplotlib`).
- Tkinter (included in standard Python installations).

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/GlucoTrack.git`.
2. Navigate to the directory: `cd GlucoTrack`.
3. Install dependencies if not already present: `pip install -r requirements.txt` (or directly as above).
4. Run the application: `python main.py`.

Note: The application creates and manages a user_logs.csv file in the datasets folder for persistent storage.

## Usage

1. Launch the application with `python main.py`.
2. Use the "Log Entry" tab to input blood sugar (numeric), select a meal, enter exercise details, and add notes. Entries are saved with timestamps.
3. In the "View Data" tab, load and display logs in a table, view statistics, and plot trends (line graph showing blood sugar over time).
4. The "Predictions" tab computes and displays a next-hour blood sugar prediction based on historical trends, adjusted for current time's circadian factor.
5. The "Advice" tab provides guidance based on the latest reading.
6. All operations include error handling for invalid inputs or insufficient data.

## Scientific Background

Diabetes management involves monitoring blood glucose, influenced by diet (via glycemic index/load), activity, and biological rhythms. GlucoTrack uses:
- Glycemic Load (GL) calculation: GL = (GI * carbs) / 100, factored into logs for future extensions.
- Linear Regression: From SciPy, to model time-series trends in blood sugar.
- Circadian Adjustments: Based on studies showing insulin resistance varies by time (e.g., higher at night), a factor (1.05 for late hours) adjusts predictions.
- Threshold Advice: Aligned with American Diabetes Association guidelines (e.g., hypoglycemia <70 mg/dL, hyperglycemia >180 mg/dL).

This provides a unique, scientifically grounded tool not commonly found in simple portfolios, emphasizing real-world applicability in personal health tech.

## Project Structure

- **main.py**: Application entry point.
- **ui.py**: Defines the graphical user interface using Tkinter.
- **data_handler.py**: Handles loading, saving, and managing CSV data for logs and foods.
- **analyzer.py**: Performs data analysis, statistics, and visualization.
- **predictor.py**: Implements prediction logic with linear regression.
- **advice.py**: Generates health advice based on readings.
- **circadian.py**: Calculates time-based metabolic adjustments.
- **utils.py**: Utility functions for timestamps, validation, and helpers.
- **datasets/foods.csv**: Preloaded food database with GI and carb values.

## License

MIT License. See LICENSE file for details (add if desired).

## Disclaimer

This is a demonstration project. Consult healthcare professionals for actual diabetes management.
