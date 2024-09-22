import pandas as pd
import numpy as np

# Load your dataset
file_path = 'filtered_job_frequency.csv'
data = pd.read_csv(file_path)

# apply np.log
data['log_frequency'] = np.log(data['frequency'])

# Save the transformed data back to a new CSV file if needed
data.to_csv('path_to_transformed_file.csv', index=False)
