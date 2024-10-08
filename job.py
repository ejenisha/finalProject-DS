import pandas as pd
import random

# Load employee data from CSV
employee_file = r'C:\Users\JenishaE\Documents\finalDS\finalProject-DS\emp_data_prep.csv'  # Path to your employee CSV file
employees_df = pd.read_csv(employee_file)
job_performance = []

for index, employee in employees_df.iterrows():
    emp_id = employee['emp_id']
    emp_name = employee['emp_name']
    
    # Generate job performance details
    no_of_projects = random.randint(1, 30)
    manager_rating = random.choice([random.randint(1, 5)] * 10)  # Allow some nulls
    
    # Determine promotion based on manager rating and number of projects
    if manager_rating is not None and manager_rating >= 3 and no_of_projects > 7:
        promotion = 1  # Set promotion to 1
    else:
        promotion = random.choice([0, 1])  # Randomly choose promotion for other cases

    # Append the record to the job_performance list
    job_performance.append({
        "emp_id": emp_id,
        "emp_name": emp_name,
        "no_of_projects": no_of_projects,
        "manager_rating": manager_rating,
        "promotion": promotion
    })

job_performance_df = pd.DataFrame(job_performance)
job_performance_df.to_csv('job_performance_data.csv', index=False)

print("Job performance data has been generated successfully and saved to job_performance_data.csv!")
