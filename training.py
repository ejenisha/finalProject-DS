import pandas as pd
import random
# Load employee data from CSV
employee_file = r'C:\Users\JenishaE\Documents\finalDS\finalProject-DS\emp_data_prep.csv'  # Path to your employee CSV file
job_performance_file = r'C:\Users\JenishaE\Documents\finalDS\job_performance_data.csv'  # Path to job performance CSV file
training_data_file = r'C:\Users\JenishaE\Documents\finalDS\finalProject-DS\training_data_prep.csv'  # Path to training data CSV file

# Read the data into DataFrames
employees_df = pd.read_csv(employee_file)
job_performance_df = pd.read_csv(job_performance_file)
training_data_df = pd.read_csv(training_data_file)

# Update project_score and hackerrank_score in training_data based on promotion status
for index, row in training_data_df.iterrows():
    emp_id = row['emp_id']
    
    # Get the promotion status from the job performance DataFrame
    promotion = job_performance_df.loc[job_performance_df['emp_id'] == emp_id, 'promotion'].values[0]
    
    # If the employee is promoted, set scores to a random value between 51 and 100
    if promotion == 1:
        training_data_df.at[index, 'project_score'] = random.randint(51, 100)  # Random score between 51 and 100
        training_data_df.at[index, 'hackerrank_score'] = random.randint(51, 100)  # Random score between 51 and 100
    else:
        training_data_df.at[index, 'project_score'] = random.randint(0, 50)  # Random score between 0 and 50
        training_data_df.at[index, 'hackerrank_score'] = random.randint(0, 50)  # Random score between 0 and 50

# Save the modified training data back to CSV
training_data_df.to_csv(training_data_file, index=False)

print("Training data scores have been modified based on promotion status successfully!")