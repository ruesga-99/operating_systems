import tkinter as tk
from tkinter import ttk

# Main Window configuration
window = tk.Tk()
window.title("Operating Systems: Multiprogramming")
window.geometry("1000x600")
window.grid_rowconfigure(0, weight = 1)        # allows the grid width to take all the available space
window.grid_columnconfigure(0, weight = 1)     # allows the gird height to take all the available space

''' Main Table
'''
cols = ("col1", "col2", "col3")                                 # stablishes the amount of columns
tree = ttk.Treeview(window, columns = cols, show = 'headings')  # tree table using the given columns

# display specific header for each column
tree.heading("col1", text = "Current Batch")
tree.heading("col2", text = "Task in Process")
tree.heading("col3", text = "Completed")

# tree table format
tree.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")

''' Control Labels
'''
time_keeper_label = tk.Label(window, text = "Elapsed Time: ") # utilizar textvariable cuado esté en constante cambio
time_keeper_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")

pending_batches_label = tk.Label(window, text = "Pending Batches: ")
pending_batches_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")

''' Input Box and Button
'''
entry_frame = tk.Frame(window)
entry_frame.grid(row=3, column=0, padx=10, pady=5, sticky="w")

entry_batches = tk.Entry(entry_frame)
entry_batches.pack(side = "left")

start_button = tk.Button(entry_frame, text = "Start", relief = "flat", activebackground = "#333C87")
start_button.pack(side = "left", padx = 10)

# Main loop
window.mainloop()