import tkinter as tk
from tkinter import ttk
from Process import *

# Global variables
elapsed_time = 0
is_paused = False
memory_size = 5
pending_tasks = []
main_memory = []
completed_tasks = []
simulation_started = False 

# This function will update the timer's label
def update_time():
    global elapsed_time
    if not is_paused:
        elapsed_time += 1
        time_keeper.config(text=f"Total Elapsed Time: {elapsed_time} s")
        process_batch()
    if pending_tasks or main_memory:
        window.after(1000, update_time)  # Update each second

# This function will udpate the remaining tasks label
def update_remaining_tasks():
    global pending_tasks, main_memory
    remaining_tasks.config(text=f"Remaining Tasks: {len(pending_tasks) + len(main_memory)}")

# Function to manage pause and continue functionality
def toggle_pause(event):
    global is_paused
    if event.char.lower() == 'p':
        is_paused = True
    elif event.char.lower() == 'c':
        is_paused = False

# Function to manage interruption events
def interruption(event):
    global main_memory
    if event.char.lower() == 'i' and main_memory and is_paused == False:
        process = main_memory.pop(0)  # Remove the first process (in execution)
        main_memory.append(process)  # Add it to the end of the in-ready list
        update_tables()  # Update tables to reflect the new state

# Function to manage error events
def error(event):
    global main_memory, completed_tasks
    if event.char.lower() == 'e' and main_memory and is_paused == False:
        process = main_memory.pop(0)  # Remove the first process (in execution)
        completed_tasks.append(process)  # Move it to the completed tasks list
        if pending_tasks:
            main_memory.append(pending_tasks.pop(0))
        update_remaining_tasks()
        update_tables()  # Update tables to reflect the new state

def process_batch():
    global main_memory, completed_tasks, pending_tasks

    # If there are loaded processes in memory
    if main_memory:
        process = main_memory[0]  # Get the first process
        process.update_time()  # Update its elapsed time
        update_tables()

        # If the process is completed
        if process.remainingT <= 0:
            completed_tasks.append(main_memory.pop(0))  # Move it to completed tasks
            
            if pending_tasks:  # If there are pending tasks
                main_memory.append(pending_tasks.pop(0))
            update_remaining_tasks()
            update_tables()

def update_tables():
    # Update Ready Table
    for row in ready_tree.get_children():
        ready_tree.delete(row)
    for process in main_memory[1:]:
        ready_tree.insert("", tk.END, values=(process.pid, process.maxT, process.elapsedT))
    
    # Update In Process Table
    for row in process_tree.get_children():
        process_tree.delete(row)
    if main_memory:
        process = main_memory[0]
        process_tree.insert("", tk.END, values=(process.pid, process.maxT, process.elapsedT, process.remainingT, process.op))
    
    # Update Completed Tasks Table
    for row in completed_tree.get_children():
        completed_tree.delete(row)
    for process in completed_tasks:
        process.solve()
        if process.maxT != process.elapsedT:
            completed_tree.insert("", tk.END, values=(process.pid, process.op, "## ERROR ##"))
        elif process.maxT == process.elapsedT:
            completed_tree.insert("", tk.END, values=(process.pid, process.op, process.result))

def start_simulation():
    global pending_tasks, main_memory, simulation_started
    
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
    update_remaining_tasks()
    main_memory = pending_tasks[:memory_size]
    pending_tasks = pending_tasks[memory_size:]
    
    # Update tables
    update_tables()

    # Disable the start button and entry field after the first use
    start_button.config(state=tk.DISABLED)
    task_entry.config(state=tk.DISABLED)
    
    # Set the flag to true
    simulation_started = True
    
    # Start the timer
    update_time()

''' Main Window General Configuration
'''
window = tk.Tk()
window.title("Operating Systems: First In First Served")
window.geometry("1200x600")
window.configure(bg="#252525")

# Bind the keys P and C to toggle_pause function
window.bind("<Key>", toggle_pause)
window.bind("<Key-i>", interruption)
window.bind("<Key-e>", error)     

''' Frames General Configuration
'''
ready_frame = tk.Frame(window, bg="#373737")
ready_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

process_frame = tk.Frame(window, bg="#373737")
process_frame.grid(row=0, column=1, pady=5, sticky="nsew")

completed_frame = tk.Frame(window, bg="#373737")
completed_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

control_frame = tk.Frame(window, bg="#373737")
control_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=(0,5), sticky="nsew")

''' In-Ready Tasks' Panel Configuration
'''
tk.Label(ready_frame, text=":::  Ready  :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, sticky="ew")

ready_tree = ttk.Treeview(ready_frame, columns=('ID', 'MT', 'ET'), show='headings', height=10)
ready_tree.heading('ID', text='ID')
ready_tree.heading('MT', text='Max Time')
ready_tree.heading('ET', text='Elapsed Time')

ready_tree.grid(row=1, padx=5, pady=5, sticky="nsew")

''' In Process Panel Configuration
'''
tk.Label(process_frame, text=":::  Task In Process  :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=0, sticky="new")

process_tree = ttk.Treeview(process_frame, columns=('ID', 'MT', 'ET', 'RT', 'OP'), show='headings', height=10)
process_tree.heading('ID', text='ID')
process_tree.heading('MT', text='Max Time')
process_tree.heading('ET', text='Elapsed Time')
process_tree.heading('RT', text='Remaining Time')
process_tree.heading('OP', text='Operation')

process_tree.grid(row=1, padx=5, pady=5, sticky="nsew")

''' Blocked Task's Panel Configuration
'''
tk.Label(process_frame, text=":::  Blocked Tasks  :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=2, sticky="new")

blocked_tree = ttk.Treeview(process_frame, columns=('ID', 'MT', 'ET', 'SRT'), show='headings', height=10)
blocked_tree.heading('ID', text='ID')
blocked_tree.heading('MT', text='Max Time')
blocked_tree.heading('ET', text='Elapsed Time')
blocked_tree.heading('SRT', text='Suspended Remaining Time')

blocked_tree.grid(row=3, padx=5, pady=5, sticky="nsew")

''' Completed Tasks' Panel Configuration
'''
tk.Label(completed_frame, text=":::  Completed Tasks  :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=0, sticky="new")

completed_tree = ttk.Treeview(completed_frame, columns=('ID', 'OP', 'RES'), show='headings', height=10)
completed_tree.heading('ID', text='ID')
completed_tree.heading('OP', text='Operation')
completed_tree.heading('RES', text='Result')

completed_tree.grid(row=1, padx=5, pady=5, sticky="nsew")

''' Control Panel Configuration
'''
tk.Label(control_frame, text=":::  P - Pause  :::  C - Continue  :::  I - Interruption  :::  E - Error  :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="w")
remaining_tasks = tk.Label(control_frame, text="Remaining Tasks: ", bg="#373737", fg="white")
remaining_tasks.grid(row=1, column=0, padx=10, pady=5, sticky="w")
time_keeper = tk.Label(control_frame, text="Total Elapsed Time: 0 s", bg="#373737", fg="white")
time_keeper.grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Label(control_frame, text="Total Tasks: ", bg="#373737", fg="white").grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Change task_entry and start_button to global variables
task_entry = tk.Entry(control_frame, width=15)
task_entry.grid(row=3, column=1, padx=5, pady=5)

start_button = tk.Button(control_frame, text="Start", bg="#46548e", fg="white", relief="flat", overrelief="flat", command=start_simulation)
start_button.grid(row=3, column=2, padx=10, pady=5)

# Expand rows and columns
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

ready_frame.grid_rowconfigure(1, weight=1)
ready_frame.grid_columnconfigure(0, weight=1)
process_frame.grid_rowconfigure(1, weight=1)
process_frame.grid_columnconfigure(0, weight=1)
completed_frame.grid_rowconfigure(1, weight=1)
completed_frame.grid_columnconfigure(0, weight=1)

# Main loop
window.mainloop()
