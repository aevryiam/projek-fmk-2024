# Data berat dan tinggi badan
weight = 70  # kg
height = 178  # cm

# Data segmen tubuh: mass percentage, length percentage, and COM position percentage
segments = {
    "Head": {"mass_percent": 8, "length_percent": 8, "COM_position_percent": 50},
    "Torso": {"mass_percent": 50, "length_percent": 50, "COM_position_percent": 40},
    "Upper Arm": {"mass_percent": 2.5, "length_percent": 11, "COM_position_percent": 50},
    "Lower Arm": {"mass_percent": 1.5, "length_percent": 7, "COM_position_percent": 50},
    "Thigh": {"mass_percent": 10, "length_percent": 23, "COM_position_percent": 40},
    "Lower Leg": {"mass_percent": 4.5, "length_percent": 15, "COM_position_percent": 40},
    "Foot": {"mass_percent": 1.5, "length_percent": 4, "COM_position_percent": 50},
}

# Perhitungan massa dan posisi COM tiap segmen
total_mass_numerator = 0
total_mass_denominator = 0

for segment, data in segments.items():
    # Hitung massa segmen
    mass = (data["mass_percent"] / 100) * weight  # kg
    
    # Hitung panjang segmen
    length = (data["length_percent"] / 100) * height  # cm
    
    # Hitung posisi COM segmen
    COM_position = (data["COM_position_percent"] / 100) * length  # cm
    
    # Jika segmen berpasangan (kiri-kanan), kalikan massa dengan 2
    if segment in ["Upper Arm", "Lower Arm", "Thigh", "Lower Leg", "Foot"]:
        mass *= 2  # karena ada 2 segmen
    
    # Akumulasi untuk perhitungan COM total
    total_mass_numerator += mass * COM_position
    total_mass_denominator += mass

# Hitung COM total
COM_total = total_mass_numerator / total_mass_denominator  # Posisi COM total dalam cm

print(f"Posisi COM Total: {COM_total:.2f} cm")
