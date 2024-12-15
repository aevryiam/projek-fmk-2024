import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
mass = 70  # Massa tubuh dalam kg
g = 9.81  # Percepatan gravitasi dalam m/s²

# Import data (waktu, percepatan, dan kecepatan)
data = pd.read_csv('iam.integral.csv')  # Ganti dengan nama file Anda
time = data['time'].values
acc_x = data['acc_x'].values  # Percepatan vertikal
velocity = data['velocity_x'].values  # Kecepatan (hasil integrasi sebelumnya)

# 3. Linear Momentum
momentum = mass * velocity
data['momentum'] = momentum  # Tambahkan ke dataframe

# 4. Normal Force dan Energi
normal_force = mass * (g + acc_x)  # Gaya normal pada kaki
energy = 0.5 * mass * velocity**2  # Energi kinetik

data['normal_force'] = normal_force  # Tambahkan ke dataframe
data['energy'] = energy  # Tambahkan ke dataframe

# Simpan hasil ke file baru
output_file = 'iam.energy.csv'
data.to_csv(output_file, index=False)
print(f"Data telah disimpan ke '{output_file}'.")

# Visualisasi Grafik
plt.figure(figsize=(12, 8))

# Grafik Linear Momentum vs Waktu
plt.subplot(3, 1, 1)
plt.plot(data['time'], data['momentum'], label='Momentum', color='blue')
plt.title('Linear Momentum vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Momentum (kg·m/s)')
plt.legend()

# Grafik Normal Force vs Waktu
plt.subplot(3, 1, 2)
plt.plot(data['time'], data['normal_force'], label='Normal Force', color='green')
plt.title('Normal Force vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Normal Force (N)')
plt.legend()

# Grafik Energi Kinetik vs Waktu
plt.subplot(3, 1, 3)
plt.plot(data['time'], data['energy'], label='Energy', color='orange')
plt.title('Kinetic Energy vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.legend()

# Tampilkan semua grafik
plt.tight_layout()
plt.show()
