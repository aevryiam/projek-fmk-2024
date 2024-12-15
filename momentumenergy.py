import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# Data
mass = 70  # Massa tubuh dalam kg
g = 9.81  # Percepatan gravitasi dalam m/s²

# Import data (waktu, percepatan, dan kecepatan)
data = pd.read_csv('data.integral.csv')  # Ganti dengan nama file yang sesuai
time = data['time'].values
acc_x = data['acc_x'].values  # Percepatan vertikal
velocity = data['velocity_x'].values  # Kecepatan (hasil integrasi sebelumnya)

# 3. Linear Momentum
momentum = mass * velocity
data['momentum'] = momentum  # Tambahkan ke dataframe

# 4. Normal Force
normal_force = mass * (g + acc_x)  # Gaya normal pada kaki
data['normal_force'] = normal_force  # Tambahkan ke dataframe

# 5. Perpindahan
# Integrasi kecepatan terhadap waktu untuk mendapatkan perpindahan
displacement = cumulative_trapezoid(velocity, time, initial=0)
data['displacement'] = displacement  # Tambahkan ke dataframe

# 6. Energi Kinetik
energy = 0.5 * mass * velocity**2  # Energi kinetik
data['energy'] = energy  # Tambahkan ke dataframe

# 7. Normal Force x Displacement
work_done = normal_force * displacement  # Gaya normal dikali perpindahan
data['work_done'] = work_done  # Tambahkan ke dataframe

# Simpan hasil ke file baru
output_file = 'data.energy_displacement.csv'
data.to_csv(output_file, index=False)
print(f"Data telah disimpan ke '{output_file}'.")

# Visualisasi Grafik - Page 1: Momentum dan Normal Force
plt.figure(figsize=(14, 8))

# Grafik Linear Momentum vs Waktu
plt.subplot(2, 1, 1)
plt.plot(data['time'], data['momentum'], label='Momentum', color='blue')
plt.title('Momentum vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Momentum (kg·m/s)')
plt.legend()

# Grafik Normal Force vs Waktu
plt.subplot(2, 1, 2)
plt.plot(data['time'], data['normal_force'], label='Normal Force', color='green')
plt.title('Normal Force vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Normal Force (N)')
plt.legend()

plt.tight_layout()
plt.show()

# Visualisasi Grafik - Page 2: Kinetic Energy dan Work Done
plt.figure(figsize=(14, 8))

# Grafik Energi Kinetik vs Waktu
plt.subplot(2, 1, 1)
plt.plot(data['time'], data['energy'], label='Kinetic Energy', color='orange')
plt.title('Kinetic Energy vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.legend()

# Grafik Work Done vs Waktu
plt.subplot(2, 1, 2)
plt.plot(data['time'], data['work_done'], label='Work Done', color='purple')
plt.title('Work Done vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Work (J)')
plt.legend()

plt.tight_layout()
plt.show()
