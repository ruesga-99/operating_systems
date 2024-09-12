import tkinter as tk
from tkinter import ttk

# Configuración de la ventana principal
window = tk.Tk()
window.title("Operating Systems: Multiprogramming")
window.geometry("1200x600")
window.configure(bg="#252525")

''' Configuración de los frames 
'''
batch_frame = tk.Frame(window, bg="#373737")
batch_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

process_frame = tk.Frame(window, bg="#373737")
process_frame.grid(row=0, column=1, pady=5, sticky="nsew")

completed_frame = tk.Frame(window, bg="#373737")
completed_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

control_frame = tk.Frame(window, bg="#373737")
control_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=(0,5), sticky="nsew")

''' Configuración de la tabla de Current Batch 
'''
tk.Label(batch_frame, text="Current Batch", bg="#373737", fg="white").grid(row=0, column=0, sticky="ew")

batch_tree = ttk.Treeview(batch_frame, columns=('ID', 'MT', 'ET'), show='headings', height=10)
batch_tree.heading('ID', text='ID')
batch_tree.heading('MT', text='Max T')
batch_tree.heading('ET', text='Elapsed T')

batch_tree.grid(row=1, padx=5, pady=5, sticky="nsew")

''' Configuración de la tabla de In Process 
'''
tk.Label(process_frame, text="Task In Process", bg="#373737", fg="white").grid(row=0, sticky="new")

process_tree = ttk.Treeview(process_frame, columns=('ID', 'MT', 'ET', 'RT', 'OP'), show='headings', height=10)
process_tree.heading('ID', text='ID')
process_tree.heading('MT', text='Max T')
process_tree.heading('ET', text='Elapsed T')
process_tree.heading('RT', text='Remaining T')
process_tree.heading('OP', text='Operation')

process_tree.grid(row=1, padx=5, pady=5, sticky="nsew")

''' Configuración de la tabla de Completed 
'''
tk.Label(completed_frame, text="Completed Tasks", bg="#373737", fg="white").grid(row=0, sticky="new")

completed_tree = ttk.Treeview(completed_frame, columns=('ID', 'OP', 'RES', 'BN'), show='headings', height=10)
completed_tree.heading('ID', text='ID')
completed_tree.heading('OP', text='Operation')
completed_tree.heading('RES', text='Result')
completed_tree.heading('BN', text='Batch No.')

completed_tree.grid(row=1, padx=5, pady=5, sticky="nsew")

''' Configuración del área de control 
'''
tk.Label(control_frame, text="P - Pause  :::  C - Continue  :::  I - Interruption  :::  E- Error", bg="#373737", fg="white").grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="w")
tk.Label(control_frame, text="Remaining Batches: ", bg="#373737", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Label(control_frame, text="Total Elapsed Time: ", bg="#373737", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Label(control_frame, text="Total Tasks: ", bg="#373737", fg="white").grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Entry(control_frame, width=15).grid(row=3, column=1, padx=5, pady=5)
tk.Button(control_frame, text="Start", bg="#46548e", fg="white", relief="flat", overrelief="flat").grid(row=3, column=2, padx=10, pady=5)

# Expandir las columnas y filas
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

batch_frame.grid_rowconfigure(1, weight=1)
batch_frame.grid_columnconfigure(0, weight=1)
process_frame.grid_rowconfigure(1, weight=1)
process_frame.grid_columnconfigure(0, weight=1)
completed_frame.grid_rowconfigure(1, weight=1)
completed_frame.grid_columnconfigure(0, weight=1)

# Main loop
window.mainloop()
