import pandas as pd
import numpy as np

# Load the data
file_path = 'iam.dinamis.csv'  # Ganti dengan lokasi file Anda
data = pd.read_csv(file_path)

# Define the conditions for modification based on time
time_threshold_running = 102
time_threshold_stationary = 132

# Copy the data to avoid modifying the original
modified_data = data.copy()

# Adjust acceleration after time 102 (simulate deceleration after running)
deceleration_indices = modified_data['time'] >= time_threshold_running
deceleration_rows = modified_data.loc[deceleration_indices, ['acc_x', 'acc_y', 'acc_z']]
scale_factors = np.linspace(1, 0, len(deceleration_rows))
modified_data.loc[deceleration_indices, ['acc_x', 'acc_y', 'acc_z']] = deceleration_rows.values * scale_factors[:, np.newaxis]

# Ensure acceleration near zero after time 132 (simulate stationary state)
stationary_indices = modified_data['time'] >= time_threshold_stationary
modified_data.loc[stationary_indices, ['acc_x', 'acc_y', 'acc_z']] = 0

# Drop unnecessary column (e.g., Unnamed: 7)
if 'Unnamed: 7' in modified_data.columns:
    modified_data = modified_data.drop(columns=['Unnamed: 7'])

# Save the modified data to a new file
modified_file_path = 'adjusted_iam_dinamis.csv'  # Ganti dengan lokasi penyimpanan file Anda
modified_data.to_csv(modified_file_path, index=False)

print(f"Modified data saved to: {modified_file_path}")
