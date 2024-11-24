import tkinter as tk
from tkinter import ttk
from Process import *
from MemFrame import *

# Global variables
elapsed_time = 0
is_paused = False
memory_size = 240
pending_tasks = []
main_memory = []
completed_tasks = []
blocked_tasks = []
simulation_started = False 
num_tasks = 0
quantum = 0

memory = []

# This function will update the timer's label
def update_time():
    global elapsed_time, blocked_tasks
    if not is_paused:
        elapsed_time += 1
        time_keeper.config(text=f"Total Elapsed Time: {elapsed_time} s")
        process_memory()

        # Update blocked processes if existent
        if blocked_tasks:
            for process in blocked_tasks:
                process.blockedT -= 1

        if main_memory:
            main_memory[0].quantum_elapsed += 1

    if pending_tasks or main_memory or blocked_tasks:
        window.after(1000, update_time)  # Update each second
        update_tables()
    else:
        # When the program has finished its execution the report is generated
        generate_PCB()

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
        process.blockedT = 7
        process.status = "Blocked"
        process.quantum_elapsed = 0
        blocked_tasks.append(process)  # Add it to the end of the in-ready list
        update_tables()  # Update tables to reflect the new state

# Function to manage error events
def error(event):
    global main_memory, completed_tasks
    if event.char.lower() == 'e' and main_memory and is_paused == False:
        process = main_memory.pop(0)  # Remove the first process (in execution)
        process.result = "## ERROR ##"
        clear_memory(process)
        completed_tasks.append(process)  # Move it to the completed tasks list
        # BCP Completition
        process.service = process.elapsedT                  # Save the service time
        process.finalization = elapsed_time                 # Save finalization time
        process.ret = process.finalization - process.arrive # Calculate and save return time
        process.wait = process.ret - process.service        # Calculate and save wait time
        process.status = "Completed: Error"

        if pending_tasks:
            new_task = pending_tasks.pop(0)
            if new_task.arrive == -1:
                new_task.arrive = elapsed_time
                new_task.status = "Ready"
            main_memory.append(new_task)
            
        update_remaining_tasks()
        update_tables()  # Update tables to reflect the new state

# Generate new process
def new_process(event):
    global main_memory, is_paused, pending_tasks, num_tasks, blocked_tasks
    if event.char.lower() == 'n' and (main_memory or blocked_tasks) and is_paused == False:
        num_tasks += 1
        new_task = generate_processes(1)[0]
        new_task.pid = num_tasks

        # If there's enough space on the memory, add it 
        if verify_availability(new_task):
            new_task.arrive = elapsed_time
            new_task.status = "Ready"
            main_memory.append(new_task)
            asign_frames(new_task)
        else:
        # If there's not enough space, add it to the pending tasks' list
            pending_tasks.append(new_task)

        update_remaining_tasks()

# Review current PCB while in execution
def view_PCB(event):
    global main_memory, blocked_tasks, is_paused
    if event.char.lower() == 'b' and (main_memory or blocked_tasks) and not is_paused:
        is_paused = True
        generate_PCB()

# Generate PCB report
def generate_PCB():
    global main_memory, completed_tasks, blocked_tasks, elapsed_time

    # Create a new window
    PCB_window = tk.Toplevel(window)
    PCB_window.title("Operating Systems: First Come First Served --- PCB")
    PCB_window.geometry("1200x600")
    PCB_window.configure(bg="#252525") 

    # Main frame
    main_frame = tk.Frame(PCB_window, bg="#373737")
    main_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    tk.Label(main_frame, text=":::  PCB Report  :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=0, sticky="new")

    # Create table to show PCB results
    PCB_tree = ttk.Treeview(main_frame, columns=('ID', 'STA', 'QET', 'AT', 'FT', 'ST', 'ResT', 'RetT', 'WT'), show='headings', height=10)
    PCB_tree.heading('ID', text='ID')
    PCB_tree.heading('STA', text='Status')
    PCB_tree.heading('QET', text='Quantum Elapsed Time')
    PCB_tree.heading('AT', text='Arrival Time')
    PCB_tree.heading('FT', text='Finalization Time')
    PCB_tree.heading('ST', text='In-Service Time')
    PCB_tree.heading('ResT', text='Response Time')
    PCB_tree.heading('RetT', text='Return Time')
    PCB_tree.heading('WT', text='Wait Time')

    PCB_tree.grid(row=1,column=0, padx=5, pady=5, sticky="nsew")

    # Information labels
    tk.Label(main_frame, text="\' *\' Indicates that the value might vary in the near future.", bg="#373737", fg="white").grid(row=2, column=0, padx=5, sticky="w")
    tk.Label(main_frame, text="\'-1\' Indicates that the value cannot be calculated at this moment.", bg="#373737", fg="white").grid(row=3, column=0, padx=5, sticky="w")

    # Expand rows and columns
    PCB_window.grid_rowconfigure(0, weight=1)
    PCB_window.grid_columnconfigure(0, weight=1)

    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    # Fill PCB_report
    for process in completed_tasks:
        PCB_tree.insert("", tk.END, values=(process.pid, process.status, "---", process.arrive, process.finalization, 
                                            process.service, process.response, process.ret, 
                                            process.wait))
    for process in main_memory:
        # Calculate estimated times
        wait = elapsed_time - process.arrive - process.elapsedT 

        if process.status == "In-Process":
            qet = f"{main_memory[0].quantum_elapsed}"
        else:
            qet = "---"

        PCB_tree.insert("", tk.END, values=(process.pid, process.status, qet, process.arrive, process.finalization, 
                                            f"{process.elapsedT} *", process.response, process.ret, 
                                            f"{wait} *"))
    for process in blocked_tasks:
        # Calculate estimated times
        wait = elapsed_time - process.arrive - process.elapsedT

        PCB_tree.insert("", tk.END, values=(process.pid, process.status, "---", process.arrive, process.finalization, 
                                            f"{process.elapsedT} *", process.response, process.ret, 
                                            f"{wait} *"))

def verify_availability(process):
    global memory, memory_size
    used = 0

    for frame in memory:
        if frame.used_space != 0:
            used += 5

    if used < memory_size:
        availiable = memory_size - used
    
    if availiable >= process.size:
        return True

    return False

def asign_frames(process):
    global memory
    process_size = process.size

    # If the whole process size has been covered, exit
    while process_size > 0:
        # Search in the whole memory for empty spaces
        for i in range (len(memory)):
            if memory[i].used_space != 0:
                continue
            else:
            # When an empty space is found, part of the process will be assigned to it
                memory[i].PID = process.pid
                memory[i].state = process.status
                if process_size >= 5:
                    memory[i].used_space = 5
                    process_size -= 5
                else:
                    memory[i].used_space = process_size
                    process_size = 0

                if process_size == 0:
                    break

def clear_memory(process):
    global memory

    # Search for all the frames used by the process and reset them
    for i in range (len(memory)):
        if memory[i].PID == process.pid:
            memory[i].reset_values()

    update_tables()

def update_memory(process):
    global memory

    # Search for all the frames used by the process and reset them
    for i in range (len(memory)):
        if memory[i].PID == process.pid:
            memory[i].state = process.status

    update_tables()

def process_memory():
    global main_memory, completed_tasks, pending_tasks, quantum, elapsed_time, memory

    # If there are loaded processes in memory
    if main_memory:
        process = main_memory[0]  # Get the first process
        if process.response == -1:
            if process.pid == 1:
                process.response = 1
            else:
                process.response = elapsed_time - process.arrive -1
        process.update_time()  # Update its elapsed time
        update_tables()

        # If the process has completed its quantum
        if process.quantum_elapsed == quantum:
            main_memory[0].status = "Ready"
            main_memory[0].quantum_elapsed = 0
            main_memory.append(main_memory.pop(0))

        # If the process is completed
        if process.remainingT <= 0:
            # BCP Completition
            process.service = process.elapsedT                  # Save the service time
            process.finalization = elapsed_time                 # Save finalization time
            process.ret = process.finalization - process.arrive # Calculate and save return time
            process.wait = process.ret - process.service        # Calculate and save wait time
            process.status = "Completed: Success"

            completed_tasks.append(process)  # Move it to completed tasks
            clear_memory(process)

            main_memory.pop(0) # delete the completed process from memory

            if pending_tasks:  # If there are pending tasks
                process = pending_tasks.pop(0)
                # Save arrival time to the memory
                if process.arrive == -1:
                    process.arrive = elapsed_time
                    process.status = "Ready"
                main_memory.append(process)
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
        process.status = "In-Process"
        process_tree.insert("", tk.END, values=(process.pid, process.maxT, process.elapsedT, 
                                                process.remainingT, process.quantum_elapsed, process.op))
    
    # Update Blocked Process Table
    for row in blocked_tree.get_children():
        blocked_tree.delete(row)
    for process in blocked_tasks:
        if process.blockedT >= 0:
            blocked_tree.insert("", tk.END, values=(process.pid, process.maxT, process.elapsedT, process.blockedT))
        else: 
            process.status = "Ready"
            main_memory.append(process)
            blocked_tasks.remove(process)

    # Update Completed Tasks Table
    for row in completed_tree.get_children():
        completed_tree.delete(row)
    for process in completed_tasks:
        if process.result == "":
            process.solve()

        completed_tree.insert("", tk.END, values=(process.pid, process.op, process.result))

    # Update Memory Frames Viewer
    for row in memory_tree.get_children():
        memory_tree.delete(row)

    for i in range(0, len(memory)//4):
        memory_tree.insert("", tk.END, values=(memory[i].toString(), memory[i+12].toString(),
                                               memory[i+24].toString(), memory[i+36].toString()))

def start_simulation():
    global pending_tasks, main_memory, simulation_started, num_tasks, quantum, memory
    
    if simulation_started:
        return  # Exit the function if the simulation has already started
    
    # Get the number of tasks from the input field
    try:
        quantum = int(quantum_entry.get())
        if quantum <= 0:
            raise ValueError("Quantum value must be greater than 0.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
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
    for task in main_memory:
        task.arrive = 0
        task.status = "Ready"
    pending_tasks = pending_tasks[memory_size:]

    # Create empty memory frames
    for i in range (0, 48):
        frame = MemFrame(i)
        
        if i <= 3:
            frame.state = "OS"
            frame.PID = "OS"
            frame.used_space = 5

        memory.append(frame)
    
    # Update tables
    update_tables()

    # Disable the start button and entry field after the first use
    start_button.config(state=tk.DISABLED)
    task_entry.config(state=tk.DISABLED)
    quantum_entry.config(state=tk.DISABLED)
    
    # Set the flag to true
    simulation_started = True
    
    # Start the timer
    update_time()

''' Main Window General Configuration
'''
window = tk.Tk()
window.title("Operating Systems: Round Robin")
window.geometry("1200x600")
window.configure(bg="#252525")

# Bind the keys P and C to toggle_pause function
window.bind("<Key>", toggle_pause)
window.bind("<Key-i>", interruption)
window.bind("<Key-e>", error)  
window.bind("<Key-n>", new_process)
window.bind("<Key-b>", view_PCB)   

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

ready_tree = ttk.Treeview(ready_frame, columns=('ID', 'MT', 'ET'), show='headings', height=1)
ready_tree.heading('ID', text='ID')
ready_tree.heading('MT', text='Max Time')
ready_tree.heading('ET', text='Elapsed Time')

ready_tree.grid(row=1, padx=5, pady=5, sticky="nsew")

''' In Process Panel Configuration
'''
tk.Label(process_frame, text=":::  Task In Process  :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=0, sticky="new")

process_tree = ttk.Treeview(process_frame, columns=('ID', 'MT', 'ET', 'RT', 'QET', 'OP'), show='headings', height=1)
process_tree.heading('ID', text='ID')
process_tree.heading('MT', text='Max Time')
process_tree.heading('ET', text='Elapsed Time')
process_tree.heading('RT', text='Remaining Time')
process_tree.heading('QET', text='Quantum Elapsed Time')
process_tree.heading('OP', text='Operation')

process_tree.grid(row=1, padx=5, pady=5, sticky="nsew")

''' Blocked Task's Panel Configuration
'''
tk.Label(process_frame, text=":::  Blocked Tasks  :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=2, sticky="new")

blocked_tree = ttk.Treeview(process_frame, columns=('ID', 'MT', 'ET', 'BRT'), show='headings', height=7)
blocked_tree.heading('ID', text='ID')
blocked_tree.heading('MT', text='Max Time')
blocked_tree.heading('ET', text='Elapsed Time')
blocked_tree.heading('BRT', text='Blocked Remaining Time')

blocked_tree.grid(row=3, padx=5, pady=5, sticky="nsew")

''' Memory Table Panel Configuration
'''
tk.Label(process_frame, text=":::  Memory   :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=4, sticky="new")

memory_tree = ttk.Treeview(process_frame, columns=('0-11', '12-23', '24-35', '36-47'), show='headings', height=13)
memory_tree.heading('0-11', text='0-11')
memory_tree.heading('12-23', text='12-23')
memory_tree.heading('24-35', text='24-35')
memory_tree.heading('36-47', text='36-47')

memory_tree.grid(row=5, padx=5, pady=5, sticky="nsew")

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
tk.Label(control_frame, text=":::  P - Pause  :::  C - Continue  :::  I - Interruption  :::  E - Error  :::  N - New Process  :::  B - BCP Status  :::  T - Pages Table  :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="w")
remaining_tasks = tk.Label(control_frame, text="Remaining Tasks: ", bg="#373737", fg="white")
remaining_tasks.grid(row=1, column=0, padx=10, pady=5, sticky="w")
time_keeper = tk.Label(control_frame, text="Total Elapsed Time: 0 s", bg="#373737", fg="white")
time_keeper.grid(row=2, column=0, padx=10, pady=5, sticky="w")

tk.Label(control_frame, text="Quantum Value: ", bg="#373737", fg="white").grid(row=1, column=1, padx=10, pady=5, sticky="w")
tk.Label(control_frame, text="Total Tasks: ", bg="#373737", fg="white").grid(row=2, column=1, padx=10, pady=5, sticky="w")

quantum_entry = tk.Entry(control_frame, width=15)
quantum_entry.grid(row=1, column=2, padx=5, pady=5)

task_entry = tk.Entry(control_frame, width=15)
task_entry.grid(row=2, column=2, padx=5, pady=5)

start_button = tk.Button(control_frame, text="Start", bg="#46548e", fg="white", relief="flat", overrelief="flat", command=start_simulation)
start_button.grid(row=1, column=3, padx=10, pady=5)

# Expand rows and columns
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

ready_frame.grid_rowconfigure(1, weight=1)
ready_frame.grid_columnconfigure(0, weight=1)

process_frame.grid_rowconfigure(0, weight=0) 
process_frame.grid_rowconfigure(1, weight=0) 
process_frame.grid_rowconfigure(2, weight=0)  
process_frame.grid_rowconfigure(3, weight=1)  
process_frame.grid_rowconfigure(4, weight=0)  
process_frame.grid_rowconfigure(5, weight=1) 
process_frame.grid_columnconfigure(0, weight=1) 

completed_frame.grid_rowconfigure(1, weight=1)
completed_frame.grid_columnconfigure(0, weight=1)

# Main loop
window.mainloop()
