
# # ~~~~~~~~~~~~~``testing code  for file exist~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # import os

# # file_path = "C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT"

# # if os.path.exists(file_path):
# #     print("File exists!")
# # else:
# #     print("File not found!")






# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import numpy as np 

# # df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)


# # timestamps = df.iloc[:, 0]  
# # breath_rate = df.iloc[:, 2]  
# # spo2 = df.iloc[:, 3] 
# # pulse = df.iloc[:, 4] 
# # body_position = df.iloc[:, 5]  
# # spo2_2 = df.iloc[:, 6]  


# # breath_rate_filtered = breath_rate.copy()  
# # breath_rate_filtered[~((breath_rate >= 80) & (breath_rate <= 100))] = np.nan




# # breath_rate_filtered = breath_rate_filtered.interpolate()

# # def save_plot(x, y, title, filename, color):
# #     plt.figure(figsize=(10, 3))
# #     plt.plot(x, y, color=color, label=title)
# #     plt.title(title)
# #     plt.legend()
# #     plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
# #     plt.close()


# # save_plot(timestamps, breath_rate_filtered, "Breath Trend Plot (Filtered 80-100)", "breath_trend", "blue")
# # save_plot(timestamps, spo2, "SpO2 Trend", "spo2_trend", "red")
# # save_plot(timestamps, pulse, "SpO2 Trend2", "spo2_trend2", "green")
# # save_plot(timestamps, body_position, "Body Position Trend", "body_position_trend", "orange")
# # save_plot(timestamps, pulse, "pulse trend", "pulse_trend_plot", "purple")



# # print("Graphs saved successfully  with filtered Breath Trend!")










# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import numpy as np 

# # df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

# # timestamps = df.iloc[:, 0]  
# # breath_rate = df.iloc[:, 2]  
# # spo2 = df.iloc[:, 3] 
# # pulse = df.iloc[:, 4] 
# # body_position = df.iloc[:, 5]  
# # other_metric = df.iloc[:, 6]  

# # # Function to filter data within range and make others blank (NaN)
# # def filter_data_within_range(data, min_val=80, max_val=100):
# #     filtered_data = data.copy()
# #     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  # Make out-of-range values NaN
# #     return filtered_data


# # breath_rate_filtered = filter_data_within_range(breath_rate)
# # spo2_filtered = filter_data_within_range(spo2)
# # spo22_filtered = filter_data_within_range(spo2,2)
# # pulse_filtered = filter_data_within_range(pulse)
# # body_position_filtered = filter_data_within_range(body_position)
# # other_metric_filtered = filter_data_within_range(other_metric)



# # def save_plot(x, y, title, filename, color):
# #     plt.figure(figsize=(10, 3))
# #     plt.plot(x, y, color=color, label=title)
# #     plt.title(title)
# #     plt.legend()
# #     plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
# #     plt.close()



# # save_plot(timestamps, breath_rate_filtered, "Breath Trend Plot (Filtered 80-100)", "breath_trend", "blue")
# # save_plot(timestamps, spo2_filtered, "SpO2 Trend (Filtered 80-100)", "spo2_trend", "red")
# # save_plot(timestamps, spo2_filtered, "spo2 Trend2 (Filtered 80-100)", "spo2_trend2", "purple")
# # save_plot(timestamps, pulse_filtered, "Pulse Trend (Filtered 80-100)", "pulse_trend", "green")
# # save_plot(timestamps, body_position_filtered, "Body Position Trend (Filtered 80-100)", "body_position_trend", "orange")

# # print("Graphs saved successfully with filtered data (only 80-100 range visible).")











# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import numpy as np

# # df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

# # timestamps = df.iloc[:, 0]  
# # breath_rate = df.iloc[:, 2]  
# # spo2 = df.iloc[:, 3]  
# # pulse = df.iloc[:, 4]  
# # body_position = df.iloc[:, 5]  
# # spo2_2 = df.iloc[:, 6]  


# # def filter_and_interpolate(data, min_val, max_val):
# #     filtered_data = data.copy()
# #     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  
# #     filtered_data = filtered_data.interpolate()
    
# #     if filtered_data.isnull().all():
# #         print(f"⚠️ Warning: No values in range {min_val}-{max_val}, using original data for graph!")
# #         return data
    
# #     return filtered_data

# # breath_rate_filtered = filter_and_interpolate(breath_rate, 80, 100)
# # spo2_filtered = filter_and_interpolate(spo2, 80, 100)
# # spo2_2_filtered = filter_and_interpolate(spo2_2, 80, 100)
# # pulse_filtered = filter_and_interpolate(pulse, 50, 150)   
# # body_position_filtered = filter_and_interpolate(body_position, 0, 150)  


# # def save_plot(x, y, title, filename, color):
# #     plt.figure(figsize=(10, 3))
# #     plt.plot(x, y, color=color, label=title)
# #     plt.title(title)


# #     if y.isnull().all():
# #         plt.ylim(0, 150)  
# #     else:
# #         plt.ylim(0, 120)  

# #     plt.legend()
# #     plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
# #     plt.close()



# # save_plot(timestamps, breath_rate_filtered, "Breath Trend (80-100)", "breath_trend", "blue")
# # save_plot(timestamps, spo2_filtered, "SpO2 Trend (80-100)", "spo2_trend", "red")
# # save_plot(timestamps, spo2_2_filtered, "SpO2 Trend2 (80-100)", "spo2_trend2", "green")
# # save_plot(timestamps, body_position_filtered, "Body Position Trend", "body_position_trend", "orange")
# # save_plot(timestamps, pulse_filtered, "Pulse Trend", "pulse_trend", "purple")

# # print("✅ All graphs saved successfully, including Pulse & Body Position Trends!")







# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import numpy as np

# # df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

# # timestamps = df.iloc[:, 0]  
# # breath_rate = df.iloc[:, 2]  
# # spo2 = df.iloc[:, 3]  
# # pulse = df.iloc[:, 4]  
# # body_position = df.iloc[:, 5]  
# # spo2_2 = df.iloc[:, 6]  

# # def filter_and_interpolate(data, min_val, max_val):
# #     filtered_data = data.copy()
# #     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  
# #     filtered_data = filtered_data.interpolate()
    
    
# #     if filtered_data.isnull().all():
# #         print(f"⚠️ Warning: No values in range {min_val}-{max_val}, using original data for graph!")
# #         return data  
    
# #     return filtered_data


# # def smooth_data(data, window_size=10):
# #     return data.rolling(window=window_size, min_periods=1).mean()  

# # breath_rate_filtered = smooth_data(filter_and_interpolate(breath_rate, 80, 100))
# # spo2_filtered = smooth_data(filter_and_interpolate(spo2, 80, 100))
# # spo2_2_filtered = smooth_data(filter_and_interpolate(spo2_2, 80, 100))
# # pulse_filtered = smooth_data(filter_and_interpolate(pulse, 50, 150))  
# # body_position_filtered = smooth_data(filter_and_interpolate(body_position, 0, 150))  


# # def save_plot(x, y, title, filename, color):
# #     plt.figure(figsize=(12, 4))  
# #     plt.plot(x, y, color=color, label=title, linewidth=2)  
# #     plt.title(title, fontsize=14)
    
    
# #     plt.grid(True, linestyle="--", alpha=0.6)
    
    
# #     if y.isnull().all():
# #         plt.ylim(0, 150)  
# #     else:
# #         plt.ylim(0, 120)  
    
# #     plt.xticks(fontsize=10, rotation=30) 
# #     plt.yticks(fontsize=10)
# #     plt.legend()
# #     plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
# #     plt.close()

# # # Save plots
# # save_plot(timestamps, breath_rate_filtered, "Breath Trend (Smoothed 80-100)", "breath_trend", "blue")
# # save_plot(timestamps, spo2_filtered, "SpO2 Trend (Smoothed 80-100)", "spo2_trend", "red")
# # save_plot(timestamps, spo2_2_filtered, "SpO2 Trend2 (Smoothed 80-100)", "spo2_trend2", "green")
# # save_plot(timestamps, body_position_filtered, "Body Position Trend (Smoothed)", "body_position_trend", "orange")
# # save_plot(timestamps, pulse_filtered, "Pulse Trend (Smoothed)", "pulse_trend", "purple")

# # print("✅ All graphs saved successfully with improved readability!")







# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import numpy as np
# # from scipy.signal import savgol_filter
# # from matplotlib.widgets import Slider

# # # Load data
# # df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

# # timestamps = df.iloc[:, 0]  
# # breath_rate = df.iloc[:, 2]  
# # spo2 = df.iloc[:, 3]  
# # pulse = df.iloc[:, 4]  
# # body_position = df.iloc[:, 5]  
# # spo2_2 = df.iloc[:, 6]  

# # def filter_and_interpolate(data, min_val, max_val):
# #     filtered_data = data.copy()
# #     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  
# #     filtered_data = filtered_data.interpolate()
    
# #     if filtered_data.isnull().all():
# #         print(f"⚠️ Warning: No values in range {min_val}-{max_val}, using original data for graph!")
# #         return data  
    
# #     return filtered_data

# # def smooth_data(data, window_size=25, polyorder=2):
# #     return savgol_filter(data, window_size, polyorder, mode='nearest')

# # breath_rate_filtered = smooth_data(filter_and_interpolate(breath_rate, 80, 100))
# # spo2_filtered = smooth_data(filter_and_interpolate(spo2, 80, 100))
# # spo2_2_filtered = smooth_data(filter_and_interpolate(spo2_2, 80, 100))
# # pulse_filtered = smooth_data(filter_and_interpolate(pulse, 50, 150))  
# # body_position_filtered = smooth_data(filter_and_interpolate(body_position, 0, 150))  

# # fig, ax = plt.subplots(5, 1, figsize=(12, 10))
# # plt.subplots_adjust(hspace=1)  

# # def plot_graph(ax, x, y, title, color):
# #     ax.plot(x, y, color=color, linewidth=2)
# #     ax.set_title(title, fontsize=14)
# #     ax.grid(True, linestyle="--", alpha=0.6)
# #     ax.set_ylim(0, max(y) + 10)

# # plot_graph(ax[0], timestamps, breath_rate_filtered, "Breath Trend (Smoothed 80-100)", "blue")
# # plot_graph(ax[1], timestamps, spo2_filtered, "SpO2 Trend (Smoothed 80-100)", "red")
# # plot_graph(ax[2], timestamps, spo2_2_filtered, "SpO2 Trend2 (Smoothed 80-100)", "green")
# # plot_graph(ax[3], timestamps, body_position_filtered, "Body Position Trend (Smoothed)", "orange")
# # plot_graph(ax[4], timestamps, pulse_filtered, "Pulse Trend (Smoothed)", "purple")


# # ax_slider = plt.axes([0.2, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
# # slider = Slider(ax_slider, 'Scroll', 0, len(timestamps)-50, valinit=0, valstep=1)

# # def update(val):
# #     pos = int(slider.val)
# #     for a in ax:
# #         a.set_xlim(timestamps[pos], timestamps[pos+50])
# #     fig.canvas.draw_idle()

# # slider.on_changed(update)

# # plt.show()









# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import numpy as np

# # df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

# # timestamps = df.iloc[:, 0]  
# # breath_rate = df.iloc[:, 2]  
# # spo2 = df.iloc[:, 3]  
# # pulse = df.iloc[:, 4]  
# # body_position = df.iloc[:, 5]  
# # spo2_2 = df.iloc[:, 6]  

# # def filter_and_interpolate(data, min_val, max_val):
# #     filtered_data = data.copy()
# #     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  
# #     filtered_data = filtered_data.interpolate()
    
    
# #     if filtered_data.isnull().all():
# #         print(f" Warning: No values in range {min_val}-{max_val}, using original data for graph!")
# #         return data  
    
# #     return filtered_data


# # def smooth_data(data, window_size=15):
# #     return data.rolling(window=window_size, min_periods=1).mean()  

# # breath_rate_filtered = smooth_data(filter_and_interpolate(breath_rate, 80, 100))
# # spo2_filtered = smooth_data(filter_and_interpolate(spo2, 80, 100))
# # spo2_2_filtered = smooth_data(filter_and_interpolate(spo2_2, 80, 100))
# # pulse_filtered = smooth_data(filter_and_interpolate(pulse, 50, 150))  
# # body_position_filtered = smooth_data(filter_and_interpolate(body_position, 0, 150))  






# # def save_plot(x, y, title, filename, color):
# #     plt.figure(figsize=(12, 4))  
# #     plt.plot(x, y, color=color, label=title, linewidth=2)  
# #     plt.title(title, fontsize=14)
    
# #     plt.grid(True, linestyle="--", alpha=0.8)
    
    
# #     if y.isnull().all():
# #         plt.ylim(0, 150)  
# #     else:
# #         plt.ylim(0, 120)  
    
# #     plt.xticks(fontsize=10, rotation=30) 
# #     plt.yticks(fontsize=10)
# #     plt.legend()
# #     plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
# #     plt.close()




# # save_plot(timestamps, breath_rate_filtered, "Breath Trend (Smoothed 80-100)", "breath_trend", "blue")
# # save_plot(timestamps, spo2_filtered, "SpO2 Trend (Smoothed 80-100)", "spo2_trend", "red")
# # save_plot(timestamps, spo2_2_filtered, "SpO2 Trend2 (Smoothed 80-100)", "spo2_trend2", "green")
# # save_plot(timestamps, body_position_filtered, "Body Position Trend (Smoothed)", "body_position_trend", "orange")
# # save_plot(timestamps, pulse_filtered, "Pulse Trend (Smoothed)", "pulse_trend", "purple")

# # print("All graphs saved successfully with improved readability!")







# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

# timestamps = df.iloc[:, 0]  
# breath_rate = df.iloc[:, 2]  
# spo2 = df.iloc[:, 3]  
# pulse = df.iloc[:, 4]  
# body_position = df.iloc[:, 5]  
# spo2_2 = df.iloc[:, 6]  

# def filter_and_interpolate(data, min_val, max_val):
#     filtered_data = data.copy()
#     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  
#     filtered_data = filtered_data.interpolate()
    
#     if filtered_data.isnull().all():
#         print(f" Warning: No values in range {min_val}-{max_val}, using original data for graph!")
#         return data  
    
#     return filtered_data

# def smooth_data(data, window_size=15):
#     return data.rolling(window=window_size, min_periods=1).mean()  

# breath_rate_filtered = smooth_data(filter_and_interpolate(breath_rate, 80, 100))
# spo2_filtered = smooth_data(filter_and_interpolate(spo2, 80, 100))
# spo2_2_filtered = smooth_data(filter_and_interpolate(spo2_2, 0, 100))
# pulse_filtered = smooth_data(filter_and_interpolate(pulse, 50, 150))  
# body_position_filtered = smooth_data(filter_and_interpolate(body_position, 0, 150))  


# window_size = 15000  
# start_index = 10   

# def save_plot(x, y, title, filename, color, start_index=0, window_size=50):
#     end_index = start_index + window_size  
    
#     plt.figure(figsize=(12, 4))  
#     plt.plot(x[start_index:end_index], y[start_index:end_index], color=color, label=title, linewidth=1)  
#     plt.title(title, fontsize=14)
    
#     plt.grid(True, linestyle="--", alpha=0.8)
    
#     if y.isnull().all():
#         plt.ylim(0, 150)  
#     else:
#         plt.ylim(0, 120)  

#     plt.xlim(x.iloc[start_index], x.iloc[end_index - 1]) 
#     plt.xticks(fontsize=10, rotation=30)  
#     plt.yticks(fontsize=10)
#     plt.legend()
#     plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
#     plt.close()



# save_plot(timestamps, breath_rate_filtered, "Breath Trend (Smoothed 80-100)", "breath_trend", "blue", start_index, window_size)
# save_plot(timestamps, spo2_filtered, "SpO2 Trend (Smoothed 80-100)", "spo2_trend", "red", start_index, window_size)
# save_plot(timestamps, spo2_2_filtered, "SpO2 Trend2 (Smoothed 80-100)", "spo2_trend2", "green", start_index, window_size)
# save_plot(timestamps, body_position_filtered, "Body Position Trend (Smoothed)", "body_position_trend", "orange", start_index, window_size)
# save_plot(timestamps, pulse_filtered, "Pulse Trend (Smoothed)", "pulse_trend", "purple", start_index, window_size)

# print(" Graphs saved with limited X-axis range!")












# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np


# df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

# timestamps = df.iloc[:, 0]  
# breath_rate = df.iloc[:, 2]  
# spo2 = df.iloc[:, 3]  
# pulse = df.iloc[:, 4]  
# body_position = df.iloc[:, 5]  
# spo2_2 = df.iloc[:, 6]  

# def filter_and_interpolate(data, min_val, max_val):
#     filtered_data = data.copy()
#     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  
#     filtered_data = filtered_data.interpolate()
    
#     if filtered_data.isnull().all():
#         print(f" Warning: No values in range {min_val}-{max_val}, using original data for graph!")
#         return data  
    
#     return filtered_data

# def smooth_data(data, window_size=15):
#     return data.rolling(window=window_size, min_periods=1).mean()  

# breath_rate_filtered = smooth_data(filter_and_interpolate(breath_rate, 80, 100))
# spo2_filtered = smooth_data(filter_and_interpolate(spo2, 80, 100))
# spo2_2_filtered = smooth_data(filter_and_interpolate(spo2_2, 0, 100))
# pulse_filtered = smooth_data(filter_and_interpolate(pulse, 50, 150))  
# # body_position_filtered = smooth_data(filter_and_interpolate(body_position, 0, 150))  


# window_size = 15000  
# start_index = 10   

# def save_plot(x, y, title, filename, color, start_index=0, window_size=50):
#     end_index = start_index + window_size  
    
#     plt.figure(figsize=(12, 4))  
#     plt.plot(x[start_index:end_index], y[start_index:end_index], color=color, label=title, linewidth=1)  
#     plt.title(title, fontsize=14)
    
#     plt.grid(True, linestyle="--", alpha=0.8)
    
#     if y.isnull().all():
#         plt.ylim(0, 150)  
#     else:
#         plt.ylim(0, 120)  

#     plt.xlim(x.iloc[start_index], x.iloc[end_index - 1]) 
#     plt.xticks(fontsize=10, rotation=30)  
#     plt.yticks(fontsize=10)
#     plt.legend()
#     plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
#     plt.close()



# save_plot(timestamps, breath_rate_filtered, "Breath Trend (Smoothed 80-100)", "breath_trend", "blue", start_index, window_size)
# save_plot(timestamps, spo2_filtered, "SpO2 Trend (Smoothed 80-100)", "spo2_trend", "red", start_index, window_size)
# save_plot(timestamps, spo2_2_filtered, "SpO2 Trend2 (Smoothed 80-100)", "spo2_trend2", "green", start_index, window_size)
# # save_plot(timestamps, body_position_filtered, "Body Position Trend (Smoothed)", "body_position_trend", "orange", start_index, window_size)
# save_plot(timestamps, pulse_filtered, "Pulse Trend (Smoothed)", "pulse_trend", "purple", start_index, window_size)

# print(" Graphs saved with limited X-axis range!")












# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np



# df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

# timestamps = df.iloc[:, 0]  
# breath_rate = df.iloc[:, 2]  
# spo2 = df.iloc[:, 3]  
# pulse = df.iloc[:, 4]  
# body_positions = df.iloc[:,5]
# spo2_2 = df.iloc[:, 6]  





# def filter_and_interpolate(data, min_val, max_val):
#     filtered_data = data.copy()
#     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  
#     filtered_data = filtered_data.interpolate()
    
#     if filtered_data.isnull().all():
#         print(f" Warning: No values in range {min_val}-{max_val}, using original data for graph!")
#         return data  
    
#     return filtered_data

# def smooth_data(data, window_size=15):
#     return data.rolling(window=window_size, min_periods=1).mean()  

# breath_rate_filtered = smooth_data(filter_and_interpolate(breath_rate, 80, 100))
# spo2_filtered = smooth_data(filter_and_interpolate(spo2, 80, 100))
# spo2_2_filtered = smooth_data(filter_and_interpolate(spo2_2, 0, 100))
# pulse_filtered = smooth_data(filter_and_interpolate(pulse, 50, 150))  
# body_position_filtered = smooth_data(filter_and_interpolate(body_position, 0, 150))  


# window_size = 15000  
# start_index = 10   

# def save_plot(x, y, title, filename, color, start_index=0, window_size=50):
#     end_index = start_index + window_size  
    
#     plt.figure(figsize=(12, 4))  
#     plt.plot(x[start_index:end_index], y[start_index:end_index], color=color, label=title, linewidth=1)  
#     plt.title(title, fontsize=14)
    
#     plt.grid(True, linestyle="--", alpha=0.8)
    
#     if y.isnull().all():
#         plt.ylim(0, 150)  
#     else:
#         plt.ylim(0, 120)  

#     plt.xlim(x.iloc[start_index], x.iloc[end_index - 1]) 
#     plt.xticks(fontsize=10, rotation=30)  
#     plt.yticks(fontsize=10)
#     plt.legend()
#     plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
#     plt.close()



# save_plot(timestamps, breath_rate_filtered, "Breath Trend (Smoothed 80-100)", "breath_trend", "blue", start_index, window_size)
# save_plot(timestamps, spo2_filtered, "SpO2 Trend (Smoothed 80-100)", "spo2_trend", "red", start_index, window_size)
# save_plot(timestamps, spo2_2_filtered, "SpO2 Trend2 (Smoothed 80-100)", "spo2_trend2", "green", start_index, window_size)
# save_plot(timestamps, body_position_filtered, "Body Position Trend (Smoothed)", "body_position_trend", "orange", start_index, window_size)
# save_plot(timestamps, pulse_filtered, "Pulse Trend (Smoothed)", "pulse_trend", "purple", start_index, window_size)

# print(" Graphs saved with limited X-axis range!")






# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import os

# # ✅ Ensure 'static' folder exists for saving the image
# save_path = "C:\\Users\\Deckmount\\Desktop\\adc_graph\\static"
# os.makedirs(save_path, exist_ok=True)

# # ✅ Dummy Data (Replace with actual CSV data)
# timestamps = np.arange(20)  # X-axis values (Time)
# body_positions = np.random.choice(["U", "L", "P", "R", "S"], size=20)  # Random body positions

# # ✅ Mapping Body Positions to Numbers (ULPRS Mapping)
# position_mapping = {"U": 5, "L": 4, "P": 3, "R": 2, "S": 1}
# numeric_positions = [position_mapping[pos] for pos in body_positions]

# # ✅ Create Figure (Bigger Size for Better Readability)
# plt.figure(figsize=(12, 5), dpi=300)

# # ✅ Line Graph (Exactly Like PDF)
# plt.plot(timestamps, numeric_positions, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6, label="Body Position")

# # ✅ Y-Axis Labels Mapping (Convert numbers back to ULPRS)
# plt.yticks(list(position_mapping.values()), list(position_mapping.keys()))  

# # ✅ Labels & Styling (Same as PDF)
# plt.title("Body Position Trend", fontsize=14)
# plt.xlabel("Time", fontsize=12)
# plt.ylabel("Body Position", fontsize=12)
# plt.grid(True, linestyle="--", alpha=0.5)  # ✅ Light Grid
# plt.legend()

# # ✅ Save Graph as PNG (High-Resolution)
# filename = os.path.join(save_path, "body_position_trend.png")
# plt.savefig(filename, bbox_inches="tight", dpi=300)  # ✅ High-Quality PNG
# plt.close()

# print(f"✅ Graph saved successfully: {filename}")






























# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

# timestamps = df.iloc[:, 0]  
# breath_rate = df.iloc[:, 2]  
# spo2 = df.iloc[:, 3]  
# pulse = df.iloc[:, 4]  
# body_position = df.iloc[:, 5]  
# spo2_2 = df.iloc[:, 6]  

# def filter_and_interpolate(data, min_val, max_val):
#     filtered_data = data.copy()
#     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan 
#     return filtered_data

# def filter_and_smooth(data, min_val, max_val, window_size=15):
#     filtered_data = data.copy()
#     filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  
#     return filtered_data.rolling(window=window_size, min_periods=1).mean()


# breath_rate_filtered = filter_and_smooth(breath_rate, 80, 100)
# spo2_filtered = (filter_and_interpolate(spo2, 80, 100))
# spo2_2_filtered = (filter_and_interpolate(spo2_2, 0, 200))
# pulse_filtered =(filter_and_interpolate(pulse, 0, 150))  
# body_position_filtered =(filter_and_interpolate(body_position, 0, 150))  



# window_size = 6000
# start_index = 10



# def save_plot(x, y, title, filename, color, start_index=0, window_size=50):
#     end_index = start_index + window_size  
#     plt.figure(figsize=(12, 4))  
#     plt.plot(x[start_index:end_index], y[start_index:end_index], color=color, label=title, linewidth=1)  
#     plt.title(title, fontsize=14)
#     plt.grid(True, linestyle="--", alpha=0.8)

#     nan_indices = y[start_index:end_index].isna()
#     nan_timestamps = x[start_index:end_index][nan_indices]

#     x_min, x_max = x.iloc[start_index], x.iloc[end_index - 1]
#     visible_nan_timestamps = [t for t in nan_timestamps if x_min <= t <= x_max]

#     for t in visible_nan_timestamps:
#         plt.vlines(t, ymin=80, ymax=100, color='orange', alpha=0.8, linewidth=0.5)

#     if y.isnull().all():
#         plt.ylim(0, 150)  
#     else:
#         plt.ylim(0, 120)  

#     plt.xlim(x_min, x_max)  
#     plt.xticks(fontsize=10, rotation=30)  
#     plt.yticks(fontsize=10)
#     plt.legend()
#     plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
#     plt.close()




# save_plot(timestamps, breath_rate_filtered, "Breath Trend (Smoothed 80-100)", "breath_trend", "blue", start_index, window_size)
# save_plot(timestamps, spo2_filtered, "SpO2 Trend (Smoothed 80-100)", "spo2_trend", "red", start_index, window_size)
# save_plot(timestamps, spo2_2_filtered, "SpO2 Trend2 (Smoothed 80-100)", "spo2_trend2", "green", start_index, window_size)
# save_plot(timestamps, body_position_filtered, "Body Position Trend (Smoothed)", "body_position_trend", "orange", start_index, window_size)
# save_plot(timestamps, pulse_filtered, "Pulse Trend (Smoothed)", "pulse_trend", "purple", start_index, window_size)


# print(" Graphs saved with limited X-axis range!")


















import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:\\Users\\Deckmount\\Downloads\\DATA0637.TXT", header=None)

timestamps = df.iloc[:, 0]  
breath_rate = df.iloc[:, 2]  
spo2 = df.iloc[:, 3]  
pulse = df.iloc[:, 4]  
body_position = df.iloc[:, 5]  
spo2_2 = df.iloc[:, 6]  

def filter_and_interpolate(data, min_val, max_val):
    filtered_data = data.copy()
    filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan 
    return filtered_data

def filter_and_smooth(data, min_val, max_val, window_size=15):
    filtered_data = data.copy()
    filtered_data[~((data >= min_val) & (data <= max_val))] = np.nan  
    return filtered_data.rolling(window=window_size, min_periods=1).mean()

breath_rate_filtered = filter_and_smooth(breath_rate, 80, 100)
spo2_filtered = filter_and_interpolate(spo2, 80, 100)
spo2_2_filtered = filter_and_interpolate(spo2_2, 0, 200)
pulse_filtered = filter_and_interpolate(pulse, 0, 150)  
body_position_filtered = filter_and_interpolate(body_position, 0, 4)  

window_size = 6000
start_index = 10

def save_plot(x, y, title, filename, color, start_index=0, window_size=50):
    end_index = start_index + window_size  
    plt.figure(figsize=(12, 4))  
    plt.plot(x[start_index:end_index], y[start_index:end_index], color=color, label=title, linewidth=1)  
    plt.title(title, fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.8)

    nan_indices = y[start_index:end_index].isna()
    nan_timestamps = x[start_index:end_index][nan_indices]

    x_min, x_max = x.iloc[start_index], x.iloc[end_index - 1]
    visible_nan_timestamps = [t for t in nan_timestamps if x_min <= t <= x_max]

    for t in visible_nan_timestamps:
        plt.vlines(t, ymin=0, ymax=20, color='orange', alpha=0.8, linewidth=0.5)

    if y.isnull().all():
        plt.ylim(0, 150)  
    else:
        plt.ylim(0, 120)  

    plt.xlim(x_min, x_max)  
    plt.xticks(fontsize=10, rotation=30)  
    plt.yticks(fontsize=10)
    plt.legend()
    plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
    plt.close()



position_labels = {0: "S", 1: "R", 2: "P", 3: "L", 4: "U"}

def save_position_plot(x, y, title, filename, color, start_index=0, window_size=50):
    end_index = start_index + window_size  
    plt.figure(figsize=(12, 4))  
    plt.plot(x[start_index:end_index], y[start_index:end_index], color=color, label=title, linewidth=2, marker="o", markersize=6)  
    plt.title(title, fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.8)

    plt.yticks(ticks=list(position_labels.keys()), labels=list(position_labels.values()))

    plt.xlim(x.iloc[start_index], x.iloc[end_index - 1])  
    plt.xticks(fontsize=10, rotation=30)  
    plt.yticks(fontsize=12)
    plt.legend()
    plt.savefig(f"static/{filename}.png", bbox_inches="tight")  
    plt.close()

save_plot(timestamps, breath_rate_filtered, "Breath Trend (Smoothed 80-100)", "breath_trend", "blue", start_index, window_size)
save_plot(timestamps, spo2_filtered, "SpO2 Trend (Smoothed 80-100)", "spo2_trend", "red", start_index, window_size)
save_plot(timestamps, spo2_2_filtered, "SpO2 Trend2 (Smoothed 80-100)", "spo2_trend2", "green", start_index, window_size)
save_position_plot(timestamps, body_position_filtered, "Body Position Trend (ULPRS)", "body_position_trend", "orange", start_index, window_size)
save_plot(timestamps, pulse_filtered, "Pulse Trend (Smoothed)", "pulse_trend", "purple", start_index, window_size)

print(" Graphs saved with ULPRS labels and improved spacing!")
