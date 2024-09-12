import tkinter as tk
from tkinter import ttk
from Process import *

# Global variables
elapsed_time = 0
is_paused = False
batch_size = 5
pending_tasks = []
current_batch = []
completed_tasks = []
simulation_started = False 
batch_number = 1  # Inicia la numeración de lotes en 1

# This function will update the timer's label
def update_time():
    global elapsed_time
    if not is_paused:
        elapsed_time += 1
        time_keeper.config(text=f"Total Elapsed Time: {elapsed_time} s")
        process_batch()
    if pending_tasks or current_batch:
        window.after(1000, update_time)  # Update each second

# Function to manage pause and continue functionality
def toggle_pause(event):
    global is_paused
    if event.char.lower() == 'p':
        is_paused = True
    elif event.char.lower() == 'c':
        is_paused = False

def process_batch():
    global current_batch, completed_tasks, pending_tasks, batch_number

    # If there are processes in the current batch
    if current_batch:
        process = current_batch[0]  # Get the first process
        process.update_time()  # Update its elapsed time
        update_tables()

        # If the process is completed
        if process.remainingT <= 0:
            process.batch = batch_number  # Asigna el número de lote al proceso completado
            completed_tasks.append(current_batch.pop(0))  # Move it to completed tasks
            update_tables()
            
            if not current_batch and pending_tasks:  # If the batch is empty and there are pending tasks
                # Load the next set of processes into the current batch
                current_batch = pending_tasks[:batch_size]
                pending_tasks = pending_tasks[batch_size:]
                batch_number += 1  # Incrementa el número de lote
                update_tables()

def update_tables():
    # Update Current Batch Table
    for row in batch_tree.get_children():
        batch_tree.delete(row)
    for process in current_batch[1:]:
        batch_tree.insert("", tk.END, values=(process.pid, process.maxT, process.elapsedT))
    
    # Update In Process Table
    for row in process_tree.get_children():
        process_tree.delete(row)
    if current_batch:
        process = current_batch[0]
        process_tree.insert("", tk.END, values=(process.pid, process.maxT, process.elapsedT, process.remainingT, process.op))
    
    # Update Completed Tasks Table
    for row in completed_tree.get_children():
        completed_tree.delete(row)
    for process in completed_tasks:
        process.solve()
        completed_tree.insert("", tk.END, values=(process.pid, process.op, process.result, process.batch))

def start_simulation():
    global pending_tasks, current_batch, simulation_started, batch_number
    
    if simulation_started:
        return  # Exit the function if the simulation has already started
    
    # Get the number of tasks from the input field
    try:
        num_tasks = int(task_entry.get())
        if num_tasks <= 0:
            raise ValueError("Number of tasks must be greater than 0.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Generate processes
    pending_tasks = generate_processes(num_tasks)
    current_batch = pending_tasks[:batch_size]
    pending_tasks = pending_tasks[batch_size:]
    
    # Update tables
    update_tables()

    # Disable the start button and entry field after the first use
    start_button.config(state=tk.DISABLED)
    task_entry.config(state=tk.DISABLED)
    
    # Set the flag to true
    simulation_started = True
    
    # Start the timer
    update_time()

''' Configuración de la ventana principal
'''
window = tk.Tk()
window.title("Operating Systems: Multiprogramming")
window.geometry("1200x600")
window.configure(bg="#252525")

# Bind the keys P and C to toggle_pause function
window.bind("<Key>", toggle_pause)

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
batch_tree.heading('MT', text='Max Time')
batch_tree.heading('ET', text='Elapsed Time')

batch_tree.grid(row=1, padx=5, pady=5, sticky="nsew")

''' Configuración de la tabla de In Process 
'''
tk.Label(process_frame, text="Task In Process", bg="#373737", fg="white").grid(row=0, sticky="new")

process_tree = ttk.Treeview(process_frame, columns=('ID', 'MT', 'ET', 'RT', 'OP'), show='headings', height=10)
process_tree.heading('ID', text='ID')
process_tree.heading('MT', text='Max Time')
process_tree.heading('ET', text='Elapsed Time')
process_tree.heading('RT', text='Remaining Time')
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
time_keeper = tk.Label(control_frame, text="Total Elapsed Time: 0 s", bg="#373737", fg="white")
time_keeper.grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Label(control_frame, text="Total Tasks: ", bg="#373737", fg="white").grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Change task_entry and start_button to global variables
task_entry = tk.Entry(control_frame, width=15)
task_entry.grid(row=3, column=1, padx=5, pady=5)

start_button = tk.Button(control_frame, text="Start", bg="#46548e", fg="white", relief="flat", overrelief="flat", command=start_simulation)
start_button.grid(row=3, column=2, padx=10, pady=5)

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
