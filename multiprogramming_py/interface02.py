import tkinter as tk
from tkinter import ttk

# Configuración de la ventana principal
window = tk.Tk()
window.title("Operating Systems: Multiprogramming")
window.geometry("1000x600")
window.configure(bg="#252525")

''' Configuración de los frames
'''
batch_frame = tk.Frame(window, bg="#6ebcbc")
batch_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

process_frame = tk.Frame(window, bg="#a76ebc")
process_frame.grid(row=0, column=1, pady=5, sticky="nsew")

completed_frame = tk.Frame(window, bg="#bca26e")
completed_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

control_frame = tk.Frame(window, bg="#bc7c6e")
control_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=(0,5), sticky="nsew")

''' Configuración de la tabla de Current Batch
'''
batch_lbl = tk.Label(batch_frame, text="Current Batch").grid(row=0, sticky="new")

''' Configuración de la tabla de In Process
'''
tk.Label(process_frame, text="Task In Process").grid(row=0, sticky="new")

''' Configuración de la tabla de Completed
'''
tk.Label(completed_frame, text="Completed Tasks").grid(row=0, sticky="new")

''' Configuración del área de control
'''
tk.Label(control_frame, text="Remaining Batches: ").grid(row=0, column=0, padx=10, pady=5, sticky="w")

tk.Label(control_frame, text="Total Elapsed Time: ").grid(row=1, column=0, padx=10, pady=5, sticky="w")

tk.Label(control_frame, text="Total Tasks: ").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Entry(control_frame, width=15).grid(row=2, column=1, padx=5, pady=5)

tk.Button(control_frame, text="Start", bg="#D35400", fg="white", relief="flat", overrelief="flat").grid(row=2, column=2, padx=10, pady=5)

# Expandir las columnas y filas
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Main loop
window.mainloop()
