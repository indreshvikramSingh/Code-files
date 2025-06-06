
import tkinter as tk
from tkinter import ttk, messagebox
import serial
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from fpdf import FPDF
import os

SERIAL_PORT = "COM5"
BAUD_RATE = 9600

data_store = {i: [] for i in range(1, 7)}
time_store = []
graph_running = True

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
except Exception as e:
    print("Serial connection error:", e)
    ser = None

def save_graph_as_pdf(signal_index, fig):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Graph {signal_index} Report", ln=True, align="C")
    
    img_path = f"graph_{signal_index}.png"
    fig.savefig(img_path)
    pdf.image(img_path, x=10, y=20, w=180)
    
    pdf.output(f"graph_{signal_index}.pdf")
    os.remove(img_path)
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



def read_serial_data():
    global data_store, time_store
    while True:
        if ser and graph_running:
            try:
                line = ser.readline().decode("utf-8").strip()
                values = line.split(',')

                if len(values) == 6:
                    float_values = [float(v) for v in values]

                    for i in range(6):
                        normalized_value = (float_values[i] - 50) / 50 
                        data_store[i+1].append(normalized_value)

                        if len(data_store[i+1]) > 1200:  # 🔥 Keep only last 500 points
                            data_store[i+1].pop(0)

                    time_store.append(len(time_store))
                    if len(time_store) > 1200:
                        time_store.pop(0)

            except Exception as e:
                print("Error reading serial:", e)

                
                
def update_graph(signal_index, selected_time, ax, canvas):
    if not time_store or not data_store[signal_index]:
        return

    max_points = 1200  # 🔥 Increase this for longer graph
    ax.clear()

    # Keep only last `max_points` values
    time_subset = time_store[-max_points:]
    data_subset = data_store[signal_index][-max_points:]

    ax.plot(time_subset, data_subset, 'g-', linewidth=2)

    if len(time_subset) > 0:
        ax.set_xlim(time_subset[0], time_subset[-1])

    ax.set_ylim(-1, 1)  
    ax.set_title(f"Signal {signal_index}")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Value")

    canvas.draw()  





def open_large_view(signal_index):
    large_window = tk.Toplevel(root)
    large_window.title(f"Large View - Signal {signal_index}")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    canvas = FigureCanvasTkAgg(fig, master=large_window)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    selected_time = selected_time_vars[signal_index - 1].get()

    def update_large_graph():
        if graph_running:
            update_graph(signal_index, selected_time, ax, canvas)
            large_window.after(500, update_large_graph)  
    
    update_large_graph()  

    control_frame = ttk.Frame(large_window)
    control_frame.pack(side="bottom", pady=5, fill="x")

    
    options = ["Infinite", "10 sec", "20 sec", "30 sec", "1 min", "5 min", "10 min"]
    large_selected_time = tk.StringVar()
    large_selected_time.set(selected_time)

    dropdown = ttk.Combobox(control_frame, textvariable=large_selected_time, values=options, state="readonly")
    dropdown.pack(side="left", padx=5)

    dropdown.bind("<<ComboboxSelected>>", lambda event, idx=signal_index: update_graph(idx, selected_option.get(), ax, canvas))


    save_button = ttk.Button(control_frame, text="Save as PDF", command=lambda: save_graph_as_pdf(signal_index, fig))
    save_button.pack(side="left", padx=5)

def toggle_graph(state):
    global graph_running
    graph_running = (state == "start")

    if graph_running:
        def continuous_update():
            if graph_running:
                for i in range(6):
                    update_graph(i+1, "Infinite", axes[i], canvases[i])
                root.after(100, continuous_update)  
        
        continuous_update()





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
    selected_option.set("infinite")
    selected_time_vars.append(selected_option)

    button_frame = ttk.Frame(control_frame)
    button_frame.pack(side="top", pady=5)

    dropdown = ttk.Combobox(button_frame, textvariable=selected_option, values=options, state="readonly")
    dropdown.pack(side="left", padx=5)

    save_button = ttk.Button(button_frame, text="Save as PDF", command=lambda: save_graph_as_pdf(signal_index, fig))
    save_button.pack(side="left", padx=5)

    dropdown.bind("<<ComboboxSelected>>", lambda event: update_graph(signal_index, selected_option.get(), ax, canvas))

    axes.append(ax)
    canvases.append(canvas)
    update_graph(signal_index, "10 sec", ax, canvas)


root = tk.Tk()
root.title("Real-Time Graphs")
root.geometry("1920x1080")  # Full HD resolution
root.state("zoomed")  # Fullscreen mode

axes = []
canvases = []

# 🔥 2 Rows × 3 Columns Layout (Properly Spread)
frame_container = tk.Frame(root)
frame_container.pack(fill="both", expand=True)


for i in range(6):
    row = i // 3  
    col = i % 3   

    frame = tk.Frame(frame_container, borderwidth=2, relief="solid")  # Frame for each graph
    frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")  # 🔥 Grid layout

    fig, ax = plt.subplots(figsize=(7, 4))  # 🔥 Bigger graph size
    canvas = FigureCanvasTkAgg(fig, frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    axes.append(ax)
    canvases.append(canvas)

for i in range(2):
    frame_container.grid_rowconfigure(i, weight=1)  
for j in range(3):
    frame_container.grid_columnconfigure(j, weight=1)  

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, pady=10, sticky="ew")

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












