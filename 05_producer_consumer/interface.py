import tkinter as tk

# Main Window General Configuration
window = tk.Tk()
window.title("Operating Systems: Producer-Consumer Algorithm")
window.geometry("1200x600")
window.configure(bg="#252525")

# Create Frames
buffer_frame = tk.Frame(window, bg="#373737")
buffer_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

information_frame = tk.Frame(window, bg="#373737")
information_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

''' Buffer's Panel Configuration '''
title_label = tk.Label(buffer_frame, text=":::      Buffer      :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold'))
title_label.grid(row=0, column=0, columnspan=20, pady=(10,40), sticky="n")

# Create a single row with evenly spaced buffer slots representation
buffer_labels = []
for i in range(20):
    lbl = tk.Label(buffer_frame, text=" ", bg="#373737", fg="white", width=4, height=2, borderwidth=2, relief="solid")
    lbl.grid(row=1, column=i, padx=2, sticky="n")
    buffer_labels.append(lbl)

''' Information's Panel Configuration 
'''
info_title_label = tk.Label(information_frame, text=":::      Information      :::", bg="#373737", fg="white", font=('Helvetica', 10, 'bold'))
info_title_label.grid(row=0, column=0, pady=10, sticky="n")

# Information labels
info_producer_lbl = tk.Label(information_frame, text="Producer: ", bg="#373737", fg="white", font=('Helvetica', 10, 'bold'))
info_producer_lbl.grid(row=1, column=0, pady=10, padx=5, sticky="nw")

info_consumer_lbl = tk.Label(information_frame, text="Consumer: ", bg="#373737", fg="white", font=('Helvetica', 10, 'bold'))
info_consumer_lbl.grid(row=2, column=0, pady=10, padx=5, sticky="nw")

info_actions_lbl = tk.Label(information_frame, text="Actions: ", bg="#373737", fg="white", font=('Helvetica', 10, 'bold'))
info_actions_lbl.grid(row=3, column=0, pady=10, padx=5, sticky="nw")

# Configure layout weights
window.grid_rowconfigure(0, weight=2)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

buffer_frame.grid_rowconfigure(0, weight=0) 
buffer_frame.grid_rowconfigure(1, weight=2)
for i in range(20):
    buffer_frame.grid_columnconfigure(i, weight=1)

information_frame.grid_rowconfigure(0, weight=0)  
information_frame.grid_rowconfigure(1, weight=0)  
information_frame.grid_rowconfigure(2, weight=0)  
information_frame.grid_rowconfigure(3, weight=0) 
information_frame.grid_columnconfigure(0, weight=1)

# Main loop
window.mainloop()
