import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumulative_trapezoid

# --- Baca Data ---
data_static = pd.read_csv('iam.statis.csv')  # Ganti dengan nama file Anda

# --- Rename Kolom ---
data_static.rename(columns={
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

# --- Variabel Waktu & Percepatan ---
time = data_static['time'].values
acc_x = data_static['acc_x'].values  # Percepatan X
acc_y = data_static['acc_y'].values  # Percepatan Y
acc_z = data_static['acc_z'].values  # Percepatan Z

# --- Integrasi Kecepatan untuk Tiap Sumbu ---
vel_x = cumulative_trapezoid(acc_x, time, initial=0)
vel_y = cumulative_trapezoid(acc_y, time, initial=0)
vel_z = cumulative_trapezoid(acc_z, time, initial=0)

# --- Magnitudo Kecepatan ---
velocity_magnitude = np.sqrt(vel_x**2 + vel_y**2 + vel_z**2)

# --- Tambahkan ke DataFrame ---
data_static['velocity_x'] = vel_x
data_static['velocity_y'] = vel_y
data_static['velocity_z'] = vel_z
data_static['velocity_magnitude'] = velocity_magnitude

# --- Momentum, Gaya Normal, dan Energi Kinetik ---
mass = 70  # Massa tubuh (kg)
g = 9.81  # Percepatan gravitasi (m/s²)

# Momentum
momentum = mass * velocity_magnitude

# Gaya Normal (berdasarkan sumbu X)
normal_force = mass * (g + acc_x)

# Energi Kinetik
kinetic_energy = 0.5 * mass * velocity_magnitude**2

# Tambahkan ke DataFrame
data_static['momentum'] = momentum
data_static['normal_force'] = normal_force
data_static['kinetic_energy'] = kinetic_energy

# --- Simpan Hasil ke CSV ---
output_file = 'iam.statis_analysis.csv'
data_static.to_csv(output_file, index=False)
print(f"Data hasil analisis telah disimpan ke '{output_file}'")

# --- Grafik Rotasi Tubuh (Roll, Pitch, Yaw) ---
plt.figure(figsize=(10, 6))
plt.plot(data_static['time'], data_static['roll'], label='Roll')
plt.plot(data_static['time'], data_static['pitch'], label='Pitch')
plt.plot(data_static['time'], data_static['yaw'], label='Yaw')
plt.title('Rotasi Tubuh (Roll, Pitch, Yaw) - Static')
plt.xlabel('Waktu (s)')
plt.ylabel('Kecepatan Sudut (rad/s)')
plt.legend()
plt.show()

# --- Grafik Percepatan Tiap Sumbu ---
plt.figure(figsize=(10, 6))
plt.plot(data_static['time'], acc_x, label='Percepatan X')
plt.plot(data_static['time'], acc_y, label='Percepatan Y')
plt.plot(data_static['time'], acc_z, label='Percepatan Z')
plt.title('Percepatan pada Tiap Sumbu')
plt.xlabel('Waktu (s)')
plt.ylabel('Percepatan (m/s²)')
plt.legend()
plt.show()

# --- Grafik Kecepatan Tiap Sumbu ---
plt.figure(figsize=(10, 6))
plt.plot(data_static['time'], vel_x, label='Kecepatan X')
plt.plot(data_static['time'], vel_y, label='Kecepatan Y')
plt.plot(data_static['time'], vel_z, label='Kecepatan Z')
plt.title('Kecepatan pada Tiap Sumbu')
plt.xlabel('Waktu (s)')
plt.ylabel('Kecepatan (m/s)')
plt.legend()
plt.show()

# --- Grafik Magnitudo Kecepatan ---
plt.figure(figsize=(10, 6))
plt.plot(data_static['time'], velocity_magnitude, label='Magnitudo Kecepatan', color='purple')
plt.title('Magnitudo Kecepatan vs Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Magnitudo Kecepatan (m/s)')
plt.legend()
plt.show()

# --- Grafik Momentum ---
plt.figure(figsize=(10, 6))
plt.plot(data_static['time'], momentum, label='Momentum', color='green')
plt.title('Momentum vs Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Momentum (kg·m/s)')
plt.legend()
plt.show()

# --- Grafik Gaya Normal ---
plt.figure(figsize=(10, 6))
plt.plot(data_static['time'], normal_force, label='Gaya Normal', color='orange')
plt.title('Gaya Normal vs Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Gaya Normal (N)')
plt.legend()
plt.show()

# --- Grafik Energi Kinetik ---
plt.figure(figsize=(10, 6))
plt.plot(data_static['time'], kinetic_energy, label='Energi Kinetik', color='red')
plt.title('Energi Kinetik vs Waktu')
plt.xlabel('Waktu (s)')
plt.ylabel('Energi Kinetik (J)')
plt.legend()
plt.show()

# --- Print Fluktuasi untuk Stabilitas ---
stability_roll_static = data_static['roll'].std()
stability_pitch_static = data_static['pitch'].std()
stability_yaw_static = data_static['yaw'].std()

print(f"Fluktuasi Roll (Static): {stability_roll_static}")
print(f"Fluktuasi Pitch (Static): {stability_pitch_static}")
print(f"Fluktuasi Yaw (Static): {stability_yaw_static}")
