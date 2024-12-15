import pandas as pd
import numpy as np

# Load the data
file_path = 'iam.dinamis.csv'  # Ganti dengan lokasi file Anda
data = pd.read_csv(file_path)

# Copy the data to avoid modifying the original
modified_data = data.copy()

# Function to repeat data if source is shorter than target
def repeat_data(source, target_length):
    repeats_needed = (target_length // len(source)) + 1  # calculate number of repeats needed
    repeated_data = pd.concat([source] * repeats_needed, ignore_index=True)  # repeat the source data
    return repeated_data.iloc[:target_length].reset_index(drop=True)  # slice to the exact target length

# Overwrite time 111-141 with time 21-51
source_1 = modified_data[(modified_data['time'] >= 21) & (modified_data['time'] <= 51)].reset_index(drop=True)
target_indices_1 = modified_data[(modified_data['time'] >= 111) & (modified_data['time'] <= 141)].index

# Repeat source_1 if needed to match target length
source_1_repeated = repeat_data(source_1, len(target_indices_1))

# Assign repeated source data to target indices
modified_data.loc[target_indices_1, ['acc_x', 'acc_y', 'acc_z', 'roll', 'pitch', 'yaw']] = source_1_repeated[['acc_x', 'acc_y', 'acc_z', 'roll', 'pitch', 'yaw']].values

# Overwrite time 132-162 with time 0-20
source_2 = modified_data[(modified_data['time'] >= 0) & (modified_data['time'] <= 20)].reset_index(drop=True)
target_indices_2 = modified_data[(modified_data['time'] >= 132) & (modified_data['time'] <= 162)].index

# Repeat source_2 if needed to match target length
source_2_repeated = repeat_data(source_2, len(target_indices_2))

# Assign repeated source data to target indices
modified_data.loc[target_indices_2, ['acc_x', 'acc_y', 'acc_z', 'roll', 'pitch', 'yaw']] = source_2_repeated[['acc_x', 'acc_y', 'acc_z', 'roll', 'pitch', 'yaw']].values

# Save the modified data to a new file
modified_file_path = 'adjusted_iam_dinamis.csv'  # Ganti dengan lokasi penyimpanan file Anda
modified_data.to_csv(modified_file_path, index=False)

print(f"Modified data saved to: {modified_file_path}")
