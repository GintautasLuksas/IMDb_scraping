import tkinter as tk
from gui_components import create_main_menu, display_top_10_submenu, display_year_vs_submenu, display_other_plots_submenu
import data_handling as dh

# Initialize the main window
root = tk.Tk()
root.title('IMDB Movie Analysis')

# Function to exit the application
def exit_application():
    root.destroy()

# Function to display main menu
def display_main_menu():
    create_main_menu(root, display_top_10_submenu, display_year_vs_submenu, display_other_plots_submenu, exit_application)

# Display the main menu initially
display_main_menu()

# Start the main loop
root.mainloop()
