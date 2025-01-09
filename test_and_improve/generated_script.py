import pandas as pd

# Define days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create an empty dictionary to store the schedule
schedule = {}

# Populate the schedule for each day 
for day in days:
    schedule[day] = {'Hour': [], 'Activity': []}

# Example data (you can customize this!)
schedule['Monday']['Hour'].extend(['9-10', '10-11', '11-12'])
schedule['Monday']['Activity'].extend(['Meeting', 'Work on Project X', 'Email'])
schedule['Tuesday']['Hour'].extend(['10-12', '1-3'])
schedule['Tuesday']['Activity'].extend(['Brainstorming', 'Client Call'])

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame.from_dict(schedule, orient='index')

# Save the DataFrame to an Excel file
df.to_excel('weekly_plan.xlsx')

print("Your weekly plan has been saved to 'weekly_plan.xlsx'")