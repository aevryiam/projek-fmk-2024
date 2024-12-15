import pandas as pd
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt
import numpy as np

# Read data file CSV
data = pd.read_csv('data.csv') # Change 'data.csv' dengan file mu

# Sesuaikan nama kolom untuk data gyroscope dan accelerometer
data.rename(columns={
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

# Declare variables
time = data['time'].values  # time
acc_x = data['acc_x'].values  # Percepatan sumbu X
acc_y = data['acc_y'].values  # Percepatan sumbu Y
acc_z = data['acc_z'].values  # Percepatan sumbu Z

# (optional) Keseragaman Waktu
if not np.allclose(np.diff(time), np.diff(time).mean()):
    print("Waktu tidak seragam, interpolasi dilakukan.")
    time_uniform = np.linspace(time.min(), time.max(), len(time))
    acc_x = np.interp(time_uniform, time, acc_x)
    acc_y = np.interp(time_uniform, time, acc_y)
    acc_z = np.interp(time_uniform, time, acc_z)
    time = time_uniform

# Calc kecepatan menggunakan integral kumulatif untuk tiap sumbu
vel_x = cumulative_trapezoid(acc_x, time, initial=0)
vel_y = cumulative_trapezoid(acc_y, time, initial=0)
vel_z = cumulative_trapezoid(acc_z, time, initial=0)

# Calc magnitudo kecepatan
velocity_magnitude = np.sqrt(vel_x**2 + vel_y**2 + vel_z**2)

# Add hasil ke DataFrame
data['velocity_x'] = vel_x
data['velocity_y'] = vel_y
data['velocity_z'] = vel_z
data['velocity_magnitude'] = velocity_magnitude

# Save hasil ke file CSV
output_file = 'data.integral.csv'
data.to_csv(output_file, index=False)
print(f"Data dengan kecepatan dan magnitudo telah disimpan ke '{output_file}'")

# Plot percepatan vs waktu untuk setiap sumbu
plt.figure(figsize=(12, 6))
plt.plot(data['time'], acc_x, label='Percepatan X (m/s²)')
plt.plot(data['time'], acc_y, label='Percepatan Y (m/s²)')
plt.plot(data['time'], acc_z, label='Percepatan Z (m/s²)')
plt.title('Percepatan vs Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Percepatan (m/s²)')
plt.legend()
plt.show()

# Plot kecepatan vs waktu untuk setiap sumbu
plt.figure(figsize=(12, 6))
plt.plot(data['time'], vel_x, label='Kecepatan X (m/s)')
plt.plot(data['time'], vel_y, label='Kecepatan Y (m/s)')
plt.plot(data['time'], vel_z, label='Kecepatan Z (m/s)')
plt.title('Kecepatan vs Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Kecepatan (m/s)')
plt.legend()
plt.show()

# Plot magnitudo kecepatan
plt.figure(figsize=(12, 6))
plt.plot(data['time'], velocity_magnitude, label='Magnitudo Kecepatan (m/s)', color='purple')
plt.title('Magnitudo Kecepatan vs Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Magnitudo Kecepatan (m/s)')
plt.legend()
plt.show()

# Plot percepatan dan kecepatan pada sumbu X dalam satu grafik
plt.figure(figsize=(12, 6))
plt.plot(data['time'], acc_x, label='Percepatan X (m/s²)', color='blue')
plt.plot(data['time'], vel_x, label='Kecepatan X (m/s)', color='red')
plt.title('Percepatan dan Kecepatan pada Sumbu X vs Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Nilai (m/s² dan m/s)')
plt.legend()
plt.show()

# Print kecepatan terakhir untuk tiap sumbu dan magnitudo
print(f"Kecepatan akhir pada sumbu X: {vel_x[-1]:.2f} m/s")
print(f"Kecepatan akhir pada sumbu Y: {vel_y[-1]:.2f} m/s")
print(f"Kecepatan akhir pada sumbu Z: {vel_z[-1]:.2f} m/s")
print(f"Magnitudo kecepatan akhir: {velocity_magnitude[-1]:.2f} m/s")