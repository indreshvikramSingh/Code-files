


# # check arduino code is running ~~~~~``


# # import serial

# # ser = serial.Serial('COM9', 9600, timeout=1) 

# # while True:
# #     line = ser.readline().decode('utf-8').strip()
# #     line = ser.readline().decode(errors='ignore').strip()

# #     if line:
# #         print(line)  


# # ~~~~~~~~~~`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``









# # for checking port 



# # import serial.tools.list_ports

# # ports = list(serial.tools.list_ports.comports())
# # for port in ports:
# #     print(port.device)

# # #################################
















import tkinter as tk
from tkinter import ttk, messagebox
import serial
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from fpdf import FPDF
import os

SERIAL_PORT = "COM6"
BAUD_RATE = 9600

latest_values = [0] * 6 


data_store = {i: [] for i in range(1, 7)}
time_store = []
graph_running = True

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
except Exception as e:
    print("Serial connection error:", e)
    ser = None

# def save_graph_as_pdf(signal_index, fig):
#     pdf = FPDF()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt=f"Graph {signal_index} Report", ln=True, align="C")
    
#     img_path = f"graph_{signal_index}.png"

    
#     plt.figure(figsize=(6, 4))
#     plt.plot(historical_time_store, historical_data_store[signal_index], 'b-', label=f"Signal {signal_index}")
#     plt.xlabel("Time (s)")
#     plt.ylabel("Value")
#     plt.title(f"Full Data Graph {signal_index}")
#     plt.legend()
#     plt.savefig(img_path)
#     plt.close()

#     pdf.image(img_path, x=10, y=20, w=180)
#     pdf.output(f"graph_{signal_index}.pdf")
#     os.remove(img_path)
#     messagebox.showinfo("PDF Saved", f"Graph {signal_index} saved as PDF")


def save_graph_as_pdf(signal_index, fig):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Graph {signal_index} Report", ln=True, align="C")

    img_path = f"graph_{signal_index}.png"

    selected_time = selected_time_vars[signal_index - 1].get()
    time_window = {"10 sec": 10, "20 sec": 20, "30 sec": 30, "1 min": 60,
                "5 min": 300, "10 min": 600}.get(selected_time, None)

    if time_window:
        start_time = time.time() - time_window
        time_range = [t for t in historical_time_store if t >= start_time]
        value_range = historical_data_store[signal_index][-len(time_range):]
    else:
        time_range = historical_time_store
        value_range = historical_data_store[signal_index]

    plt.figure(figsize=(6, 4))
    if len(time_range) > 0 and len(value_range) > 0:
        plt.plot(time_range, value_range, 'b-', label=f"Signal {signal_index}")
        plt.xlabel("Time (s)")
        plt.ylabel("Value")
        plt.title(f"Graph {signal_index} Report")
        plt.legend()
        plt.savefig(img_path)
        plt.close()

        pdf.image(img_path, x=10, y=20, w=180)
        os.remove(img_path)

    pdf.output(f"graph_{signal_index}.pdf")
    messagebox.showinfo("PDF Saved", f"Graph {signal_index} saved as PDF")



def save_all_graphs_as_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="All Graphs Report", ln=True, align="C")

    fig, axs = plt.subplots(6, 1, figsize=(8, 12))  

    for i in range(6):
        axs[i].plot(time_store, data_store[i+1], label=f"Signal {i+1}", color='b')
        axs[i].set_title(f"Graph {i+1}")
        axs[i].set_xlabel("Time (s)")
        axs[i].set_ylabel("Value")
        axs[i].legend(loc="upper right")
        axs[i].set_ylim(0, 100)

    plt.tight_layout()

    img_path = "all_graphs.png"
    fig.savefig(img_path)

    pdf.image(img_path, x=10, y=20, w=180)
    os.remove(img_path)  

    pdf.output("All_Graphs.pdf")
    messagebox.showinfo("PDF Saved", "All graphs saved as a single PDF")



historical_data_store = {i: [] for i in range(1, 7)} 
historical_time_store = [] 




def read_serial_data():
    global latest_values

    while graph_running and ser: 
        try:
            line = ser.readline().decode("utf-8").strip()
            values = line.split(',')
            if len(values) == 6:
                latest_values = [float(v) for v in values]

                current_time = time.time()
                time_store.append(current_time)
                historical_time_store.append(current_time)

                for i in range(1, 7):
                    data_store[i].append(latest_values[i - 1])
                    historical_data_store[i].append(latest_values[i - 1])

        except Exception as e:
            print("Error reading serial data:", e)
        
        time.sleep(0.1) 


def update_all_graphs():
    """ Update all graphs in the main thread only if graph_running is True """
    if graph_running:  
        for i in range(6):
            update_graph(i + 1, axes[i], canvases[i], selected_time_vars[i].get())
        root.after(500, update_all_graphs)  





def update_graph(i, ax, canvas, selected_time):
    ax.clear()  
    ax.set_title(f"Signal {i}")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Value")

    
    if selected_time == "Infinite":
        time_range = historical_time_store
        value_range = historical_data_store[i]
    else:
        time_window = {"10 sec": 10, "20 sec": 20, "30 sec": 30, "1 min": 60,
                    "5 min": 300, "10 min": 600}.get(selected_time, 10)
        start_time = time.time() - time_window
        time_range = [t for t in historical_time_store if t >= start_time]
        value_range = historical_data_store[i][-len(time_range):]

    
    if len(time_range) > 0 and len(value_range) > 0:
        ax.plot(time_range, value_range, 'b-', label=f"Signal {i}")
        ax.legend()
    
    canvas.draw()  










def open_large_view(signal_index):
    large_window = tk.Toplevel(root)
    large_window.title(f"Large View - Signal {signal_index}")
    
    fig, ax = plt.subplots(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master=large_window)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    selected_time = selected_time_vars[signal_index - 1].get()
    large_selected_time = tk.StringVar()
    large_selected_time.set(selected_time)
    
    def update_large_graph():
        if graph_running:  
            update_graph(signal_index, ax, canvas, large_selected_time.get())  
        large_window.after(500, update_large_graph)  
    
    update_large_graph()  
    
    control_frame = ttk.Frame(large_window)
    control_frame.pack(side="bottom", pady=5, fill="x")
    
    options = ["Infinite", "10 sec", "20 sec", "30 sec", "1 min", "5 min", "10 min"]
    dropdown = ttk.Combobox(control_frame, textvariable=large_selected_time, values=options, state="readonly")
    dropdown.pack(side="left", padx=5)
    
    dropdown.bind("<<ComboboxSelected>>", lambda event: update_graph(signal_index, ax, canvas, large_selected_time.get()))
    
    save_button = ttk.Button(control_frame, text="Save as PDF", command=lambda: save_graph_as_pdf(signal_index, fig))
    save_button.pack(side="left", padx=5)






def toggle_graph(state):
    global graph_running
    graph_running = (state == "start")
    
    if graph_running:
        update_all_graphs()  








selected_time_vars = []

def create_graph_with_dropdown(root, signal_index, row, col):
    frame = ttk.Frame(root)
    frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    
    fig, ax = plt.subplots(figsize=(2, 1.5))
    ax.set_title(f"Signal {signal_index}")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Value")
    
    canvas = FigureCanvasTkAgg(fig, frame)
    graph_widget = canvas.get_tk_widget()
    graph_widget.pack(side="top", fill="both", expand=True)
    graph_widget.bind("<Button-1>", lambda event: open_large_view(signal_index))
    
    control_frame = ttk.Frame(frame)
    control_frame.pack(side="bottom", pady=5, fill="x")
    
    options = ["Infinite", "10 sec", "20 sec", "30 sec", "1 min", "5 min", "10 min"]
    selected_option = tk.StringVar()
    selected_option.set("Infinite")  
    selected_time_vars.append(selected_option)
    
    button_frame = ttk.Frame(control_frame)
    button_frame.pack(side="top", pady=5)
    
    dropdown = ttk.Combobox(button_frame, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(side="left", padx=5)
    
    save_button = ttk.Button(button_frame, text="Save as PDF", command=lambda: save_graph_as_pdf(signal_index, fig))
    save_button.pack(side="left", padx=5)
    
    dropdown.bind("<<ComboboxSelected>>", lambda event: update_graph(signal_index, ax, canvas, selected_option.get()))
    
    
    axes.append(ax)
    canvases.append(canvas)
    
    
    
    
    
    
    
    
root = tk.Tk()
root.title("Real-Time Graphs")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

axes = []
canvases = []
for i in range(6):
    create_graph_with_dropdown(root, i+1, i//2, i%2)

button_frame = ttk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

start_button = ttk.Button(button_frame, text="Start Graph", command=lambda: toggle_graph("start"))
start_button.pack(side="left", padx=10)

stop_button = ttk.Button(button_frame, text="Stop Graph", command=lambda: toggle_graph("stop"))
stop_button.pack(side="right", padx=10)

save_all_button = ttk.Button(button_frame, text="Save All Graphs as PDF", command=save_all_graphs_as_pdf)
save_all_button.pack(side="left", padx=10)


serial_thread = threading.Thread(target=read_serial_data, daemon=True)
serial_thread.start()
toggle_graph("start")

root.mainloop()
