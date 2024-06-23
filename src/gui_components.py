import tkinter as tk
import data_handling as dh

def display_main_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Select a category to display:")
    label.pack()

    top10_button = tk.Button(root, text="Category: Top 10", command=lambda: display_top_10_submenu(root))
    top10_button.pack(pady=10)

    year_comparison_button = tk.Button(root, text="Category: Year Comparison", command=lambda: display_year_vs_submenu(root))
    year_comparison_button.pack(pady=10)

    other_plots_button = tk.Button(root, text="Others (All other plots)", command=lambda: display_other_plots_submenu(root))
    other_plots_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=10)

def display_top_10_submenu(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Select a Top 10 Movies option:")
    label.pack()

    button1 = tk.Button(root, text="Top 10 Movies by Rating", command=dh.show_top_10_movies_by_rating)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Top 10 Movies by Rating Amount", command=dh.show_top_10_movies_by_rating_amount)
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Top 10 Movies by Length", command=dh.show_top_10_movies_by_length)
    button3.pack(pady=10)

    back_button = tk.Button(root, text="Back to Main Menu", command=lambda: display_main_menu(root))
    back_button.pack(pady=10)

def display_year_vs_submenu(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Select a Year vs ... option:")
    label.pack()

    button1 = tk.Button(root, text="Average Rating by Year", command=dh.show_year_vs_rating)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Average Length (in minutes) by Year", command=dh.show_year_vs_length)
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Average Rating Amount by Year", command=dh.show_year_vs_rating_amount)
    button3.pack(pady=10)

    back_button = tk.Button(root, text="Back to Main Menu", command=lambda: display_main_menu(root))
    back_button.pack(pady=10)

def display_other_plots_submenu(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Select an Other Plot option:")
    label.pack()

    button1 = tk.Button(root, text="Number of Movies by Year", command=lambda: dh.show_other_plots(1))
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Distribution of Ratings", command=lambda: dh.show_other_plots(2))
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Rating Distribution by Duration Category", command=lambda: dh.show_other_plots(4))
    button3.pack(pady=10)

    button4 = tk.Button(root, text="Average Rating by Year", command=lambda: dh.show_other_plots(5))
    button4.pack(pady=10)

    button5 = tk.Button(root, text="Number of Movies by MovieGroup", command=lambda: dh.show_other_plots(6))
    button5.pack(pady=10)

    back_button = tk.Button(root, text="Back to Main Menu", command=lambda: display_main_menu(root))
    back_button.pack(pady=10)
