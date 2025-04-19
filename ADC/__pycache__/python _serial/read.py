# import serial
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# ser = serial.Serial( 'COM3 ',9600, timeout=1)


# x_data = []
# y_data = []
# index = 0

# fig, ax = plt.subplots()
# line, = ax.plot([], [], marker='o', linestyle='-', color='b')

# ax.set_title("Real-Time Sensor Data Plot")
# ax.set_xlabel("Time (samples)")
# ax.set_ylabel("Sensor Value")
# ax.grid(True)
# ax.set_ylim(0, 110) 

# def update(frame):
#     global index
#     if ser.in_waiting > 0:
#         try:
#             value = ser.readline().decode('utf-8').strip()
#             if value:
#                 y_data.append(float(value))  
#                 x_data.append(index)
#                 index += 1  

               
#                 if len(x_data) > 50:
#                     x_data.pop(0)
#                     y_data.pop(0)

               
#                 line.set_data(x_data, y_data)
#                 ax.set_xlim(max(0, index - 50), index + 5)  

#         except Exception as e:
#             print(f"Error: {e}")

#     return line
# ani = animation.FuncAnimation(fig, update, interval=500, blit=False)

# plt.show()