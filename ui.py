import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import data_handler
import analyzer
import predictor
import advice
import utils

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GlucoTrack: Diabetes Management Assistant")
        self.geometry("900x700")
        self.foods = data_handler.load_foods()
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)
        self.create_logging_tab()
        self.create_view_tab()
        self.create_predict_tab()
        self.create_advice_tab()

    def create_logging_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Log Entry')
        ttk.Label(tab, text="Blood Sugar (mg/dL):").grid(row=0, column=0, padx=10, pady=5)
        self.bs_entry = ttk.Entry(tab)
        self.bs_entry.grid(row=0, column=1)
        ttk.Label(tab, text="Meal:").grid(row=1, column=0, padx=10, pady=5)
        self.meal_combo = ttk.Combobox(tab, values=self.foods['food'].tolist(), width=30)
        self.meal_combo.grid(row=1, column=1)
        ttk.Label(tab, text="Exercise (e.g., walking 30 min):").grid(row=2, column=0, padx=10, pady=5)
        self.ex_entry = ttk.Entry(tab)
        self.ex_entry.grid(row=2, column=1)
        ttk.Label(tab, text="Notes:").grid(row=3, column=0, padx=10, pady=5)
        self.notes_entry = ttk.Entry(tab)
        self.notes_entry.grid(row=3, column=1)
        ttk.Button(tab, text="Save Entry", command=self.save_entry).grid(row=4, column=0, columnspan=2, pady=10)

    def save_entry(self):
        try:
            bs = utils.validate_input(self.bs_entry.get(), float)
            if bs <= 0:
                raise ValueError("Blood sugar must be positive.")
            meal = self.meal_combo.get()
            ex = self.ex_entry.get()
            notes = self.notes_entry.get()
            timestamp = utils.get_current_timestamp()
            entry = {'timestamp': timestamp, 'blood_sugar': bs, 'meal': meal, 'exercise': ex, 'notes': notes}
            data_handler.save_log(entry)
            tk.messagebox.showinfo("Success", "Entry saved successfully.")
            self.bs_entry.delete(0, tk.END)
            self.meal_combo.set('')
            self.ex_entry.delete(0, tk.END)
            self.notes_entry.delete(0, tk.END)
        except ValueError as e:
            tk.messagebox.showerror("Input Error", str(e))

    def create_view_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='View Data')
        columns = ('timestamp', 'blood_sugar', 'meal', 'exercise', 'notes', 'glycemic_load')
        self.data_tree = ttk.Treeview(tab, columns=columns, show='headings')
        for col in columns:
            self.data_tree.heading(col, text=col.capitalize())
        self.data_tree.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)
        ttk.Button(tab, text="Load Data", command=self.load_data).grid(row=1, column=0, pady=5)
        self.stats_label = ttk.Label(tab, text="")
        self.stats_label.grid(row=2, column=0, pady=5)
        self.plot_frame = ttk.Frame(tab)
        self.plot_frame.grid(row=0, column=1, rowspan=3, sticky='nsew', padx=10)
        ttk.Button(tab, text="Plot Trends", command=self.plot_data).grid(row=1, column=1, pady=5)

    def load_data(self):
        data = data_handler.load_logs()
        self.data_tree.delete(*self.data_tree.get_children())
        for _, row in data.iterrows():
            self.data_tree.insert('', 'end', values=(row['timestamp'], row['blood_sugar'], row['meal'], row['exercise'], row['notes'], row.get('glycemic_load', 0)))
        stats = analyzer.get_stats(data)
        self.stats_label.config(text=f"Statistics:\n{stats}")

    def plot_data(self):
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        data = data_handler.load_logs()
        canvas = analyzer.plot_trends(data, self.plot_frame)
        if canvas:
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)

    def create_predict_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Predictions')
        self.predict_label = ttk.Label(tab, text="Click to generate prediction.", wraplength=400)
        self.predict_label.pack(padx=10, pady=20)
        ttk.Button(tab, text="Generate Prediction", command=self.do_predict).pack(pady=10)

    def do_predict(self):
        data = data_handler.load_logs()
        pred = predictor.predict_next(data)
        self.predict_label.config(text=pred)

    def create_advice_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Advice')
        self.advice_label = ttk.Label(tab, text="Click to get advice based on latest reading.", wraplength=400)
        self.advice_label.pack(padx=10, pady=20)
        ttk.Button(tab, text="Get Advice", command=self.get_advice).pack(pady=10)

    def get_advice(self):
        data = data_handler.load_logs()
        if data.empty:
            advice_text = "No data available for advice."
        else:
            last_bs = data.iloc[-1]['blood_sugar']
            advice_text = advice.get_advice(last_bs)
        self.advice_label.config(text=advice_text)
