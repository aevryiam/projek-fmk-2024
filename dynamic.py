import pandas as pd
import matplotlib.pyplot as plt

# import data
data_dynamic = pd.read_csv('data.csv')  # Pastikan file CSV sesuai format

# Sesuaikan nama kolom untuk data gyroscope dan accelerometer
data_dynamic.rename(columns={
    'wx (rad/s)': 'roll', 
    'wy (rad/s)': 'pitch', 
    'wz (rad/s)': 'yaw',
    'wz' : 'roll',
    'wy' : 'pitch',
    'wx' : 'yaw',
    'ax' : 'acc_x',
    'ay' : 'acc_y',
    'az' : 'acc_z'
}, inplace=True)

# Plot data gyroscope untuk eksperimen dynamic (roll, pitch, yaw)
plt.figure(figsize=(10, 6))
plt.plot(data_dynamic['time'], data_dynamic['roll'], label='Roll')
plt.plot(data_dynamic['time'], data_dynamic['pitch'], label='Pitch')
plt.plot(data_dynamic['time'], data_dynamic['yaw'], label='Yaw')
plt.title('Rotasi Tubuh (Roll, Pitch, Yaw) - Dynamic')
plt.xlabel('Waktu (s)')
plt.ylabel('Sudut (derajat)')
plt.legend()
plt.show()

# Fluktuasi (standard deviation) untuk stabilitas dalam eksperimen dynamic
stability_roll_dynamic = data_dynamic['roll'].std()
stability_pitch_dynamic = data_dynamic['pitch'].std()
stability_yaw_dynamic = data_dynamic['yaw'].std()

print(f"Fluktuasi Roll (Dynamic): {stability_roll_dynamic}")
print(f"Fluktuasi Pitch (Dynamic): {stability_pitch_dynamic}")
print(f"Fluktuasi Yaw (Dynamic): {stability_yaw_dynamic}")

# Plot percepatan pada sumbu Z selama langkah (gunakan data accelerometer untuk Z)
plt.figure(figsize=(10, 6))
plt.plot(data_dynamic['time'], data_dynamic['acc_z'], label='Percepatan Z')
plt.title('Percepatan Z Selama Langkah (Dynamic)')
plt.xlabel('Waktu (s)')
plt.ylabel('Percepatan (m/s^2)')
plt.legend()
plt.show()