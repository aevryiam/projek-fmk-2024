import pandas as pd

# Data segmen tubuh dalam meter
data = {
    'Segment': ['Head', 'Torso', 'Upper Arm', 'Lower Arm', 'Thigh', 'Lower Leg', 'Foot'],
    'Mass (kg)': [5.6, 35.0, 3.5, 2.1, 14.0, 6.3, 2.1],
    'Length (m)': [14.4 / 100, 90.0 / 100, 19.8 / 100, 12.6 / 100, 41.4 / 100, 27.0 / 100, 7.2 / 100],  # Mengubah cm ke meter
    'COM Position (m)': [7.2 / 100, 36.0 / 100, 9.9 / 100, 6.3 / 100, 16.56 / 100, 10.8 / 100, 3.6 / 100]  # Mengubah cm ke meter
}

# Konversi ke DataFrame
df = pd.DataFrame(data)

# Tambahkan kontribusi COM global untuk setiap segmen
# Asumsi: Posisi COM dihitung relatif terhadap titik awal tubuh (misalnya dari tumit)
df['Global COM Contribution'] = df['Mass (kg)'] * df['COM Position (m)']

# Hitung total massa dan total kontribusi COM
total_mass = df['Mass (kg)'].sum()
total_contribution = df['Global COM Contribution'].sum()

# Hitung COM global tubuh
global_com = total_contribution / total_mass

# Tampilkan hasil
print("Data Segmen Tubuh:")
print(df)
print(f"\nTotal Massa Tubuh: {total_mass:.2f} kg")
print(f"Global Center of Mass (COM): {global_com:.2f} m dari titik referensi")
