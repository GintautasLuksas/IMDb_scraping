import tkinter as tk
import matplotlib.pyplot as plt
import seaborn as sns
import data_handling as dh

def create_main_menu(root, show_top10_callback, show_year_vs_callback, show_other_callback, exit_callback):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select a category to display:").pack()

    tk.Button(root, text="Category: Top 10", command=lambda: show_top10_callback(root)).pack(pady=10)
    tk.Button(root, text="Category: Year Comparison", command=lambda: show_year_vs_callback(root)).pack(pady=10)
    tk.Button(root, text="Others (All other plots)", command=lambda: show_other_callback(root)).pack(pady=10)
    tk.Button(root, text="Exit", command=exit_callback).pack(pady=10)

def display_top_10_submenu(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select a Top 10 Movies option:").pack()

    tk.Button(root, text="Top 10 Movies by Rating", command=dh.show_top_10_movies_by_rating).pack(pady=10)

    tk.Button(root, text="Top 10 Movies by Rating Amount", command=dh.show_top_10_movies_by_rating_amount).pack(pady=10)

    tk.Button(root, text="Top 10 Movies by Length", command=dh.show_top_10_movies_by_length).pack(pady=10)

    tk.Button(root, text="Back to Main Menu", command=lambda: create_main_menu(root, display_top_10_submenu, display_year_vs_submenu, display_other_plots_submenu, exit_application)).pack(pady=10)

def display_year_vs_submenu(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select a Year vs ... option:").pack()

    tk.Button(root, text="Average Rating by Year", command=dh.show_year_vs_rating).pack(pady=10)

    tk.Button(root, text="Average Length (in minutes) by Year", command=dh.show_year_vs_length).pack(pady=10)

    tk.Button(root, text="Average Rating Amount by Year", command=dh.show_year_vs_rating_amount).pack(pady=10)

    tk.Button(root, text="Back to Main Menu", command=lambda: create_main_menu(root, display_top_10_submenu, display_year_vs_submenu, display_other_plots_submenu, exit_application)).pack(pady=10)

def display_other_plots_submenu(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select an Other Plot option:").pack()

    tk.Button(root, text="Number of Movies by Year", command=lambda: dh.show_other_plots(1)).pack(pady=10)

    tk.Button(root, text="Distribution of Ratings", command=lambda: dh.show_other_plots(2)).pack(pady=10)

    tk.Button(root, text="Rating Distribution by Duration Category", command=lambda: dh.show_other_plots(4)).pack(pady=10)

    tk.Button(root, text="Average Rating by Year", command=lambda: dh.show_other_plots(5)).pack(pady=10)

    tk.Button(root, text="Number of Movies by MovieGroup", command=lambda: dh.show_other_plots(6)).pack(pady=10)

    tk.Button(root, text="Back to Main Menu", command=lambda: create_main_menu(root, display_top_10_submenu, display_year_vs_submenu, display_other_plots_submenu, exit_application)).pack(pady=10)

def exit_application(root):
    root.destroy()
