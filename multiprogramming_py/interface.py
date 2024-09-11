import tkinter as tk
from tkinter import ttk

# Main Window configuration
window = tk.Tk()
window.title("Operating Systems: Multiprogramming")
window.geometry("1000x600")

# Main table
columns = ("col1", "col2", "col3")
tree = ttk.Treeview(window, columns = columns, show = 'headings')

tree.heading("col1", text = "Pending")
tree.heading("col2", text = "Processing")
tree.heading("col3", text = "Completed")

tree.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")

time_keeper_label = tk.Label(window, text = "Elapsed Time: ") # utilizar textvariable cuado esté en constante cambio
time_keeper_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")

pending_batches_label = tk.Label(window, text = "Pending Batches: ")
pending_batches_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")

entry_frame = tk.Frame(window)
entry_frame.grid(row=3, column=0, padx=10, pady=5, sticky="w")

entry_batches = tk.Entry(entry_frame)
entry_batches.pack(side = "left")

start_button = tk.Button(entry_frame, text = "Start")
start_button.pack(side = "left", padx = 10)

window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)

# Main loop
window.mainloop()