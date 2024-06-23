import tkinter as tk
import gui_components as gui

# Initialize the main window
root = tk.Tk()
root.title('IMDB Movie Analysis')

# Display the main menu initially
gui.display_main_menu(root)

# Start the main loop
root.mainloop()
