import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Baca data dari file CSV
data = pd.read_csv('data_acc.csv')  # Ganti dengan nama file Anda

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

# Pastikan kolom percepatan tersedia
if 'acc_x' in data.columns and 'acc_y' in data.columns and 'acc_z' in data.columns:
    # Hitung magnitudo percepatan
    data['acc_magnitude'] = np.sqrt(data['acc_x']**2 + data['acc_y']**2 + data['acc_z']**2)
    
    # Simpan hasil ke file baru
    data.to_csv('output_acc_magnitude.csv', index=False)
    print("Data dengan magnitudo percepatan telah disimpan ke 'output_acc_magnitude.csv'.")

    # Plot magnitudo percepatan terhadap waktu
    plt.figure(figsize=(10, 6))
    plt.plot(data['time'], data['acc_magnitude'], label='Magnitudo Percepatan', color='purple')
    plt.title('Magnitudo Percepatan vs Waktu')
    plt.xlabel('Waktu (s)')
    plt.ylabel('Magnitudo Percepatan (m/s²)')
    plt.legend()
    plt.grid()
    plt.show()

else:
    print("Kolom percepatan (acc_x, acc_y, acc_z) tidak ditemukan dalam file.")