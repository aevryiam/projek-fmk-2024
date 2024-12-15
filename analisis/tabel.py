# Input berat dan tinggi badan
weight = float(input("Masukkan berat badan Anda (kg): "))
height = float(input("Masukkan tinggi badan Anda (cm): "))

# Data segmen tubuh dengan input panjang segmen
segments = {
    "Head": {"mass_percent": 8, "length_percent": None, "COM_position_percent": 50},
    "Torso": {"mass_percent": 50, "length_percent": None, "COM_position_percent": 40},
    "Upper Arm": {"mass_percent": 2.5, "length_percent": None, "COM_position_percent": 50},
    "Lower Arm": {"mass_percent": 1.5, "length_percent": None, "COM_position_percent": 50},
    "Thigh": {"mass_percent": 10, "length_percent": None, "COM_position_percent": 40},
    "Lower Leg": {"mass_percent": 4.5, "length_percent": None, "COM_position_percent": 40},
    "Foot": {"mass_percent": 1.5, "length_percent": None, "COM_position_percent": 50},
}

# Input panjang segmen untuk setiap bagian tubuh
for segment in segments.keys():
    segments[segment]["length_percent"] = float(
        input(f"Masukkan panjang segmen {segment} (cm, dari total tinggi badan): ")
    ) / height * 100  # Konversi ke persentase

# Perhitungan massa dan posisi COM tiap segmen
results = []
total_mass_COM = 0  # Total massa * posisi COM
total_mass = 0  # Total massa tubuh
reference_point = 0  # Titik referensi (dalam cm dari lantai)

for segment, data in segments.items():
    # Hitung massa segmen
    mass = (data["mass_percent"] / 100) * weight  # kg
    
    # Hitung panjang segmen
    length = (data["length_percent"] / 100) * height  # cm
    
    # Hitung posisi COM segmen relatif terhadap lantai (referensi)
    COM_position = reference_point + (data["COM_position_percent"] / 100) * length  # cm
    
    # Jika segmen berpasangan (kiri-kanan), kalikan massa dengan 2
    if segment in ["Upper Arm", "Lower Arm", "Thigh", "Lower Leg", "Foot"]:
        mass *= 2  # karena ada 2 segmen
    
    # Tambahkan ke total massa dan total massa * posisi
    total_mass += mass
    total_mass_COM += mass * COM_position
    
    # Update titik referensi untuk segmen berikutnya
    reference_point += length
    
    # Simpan hasil
    results.append({
        "Segment": segment,
        "Mass (kg)": round(mass, 2),
        "Length (cm)": round(length, 2),
        "COM Position (cm)": round(COM_position, 2)
    })

# Hitung posisi COM total
COM_total = total_mass_COM / total_mass

# Tampilkan hasil
import pandas as pd
df_results = pd.DataFrame(results)
print(df_results)
print(f"\nCenter of Mass (COM) total adalah {COM_total:.2f} cm dari lantai.")
