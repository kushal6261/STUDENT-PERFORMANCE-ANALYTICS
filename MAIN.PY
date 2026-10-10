import pandas as pd
import numpy as np

def assign_grade(percentage):
    if percentage >= 80:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 40:
        return 'C'
    else:
        return 'F'

print("\n" + "="*75)
print("              EWB STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("="*75)

print("\n--- 1. Loading Student Data ---")
df = pd.read_csv('STUDENT.CSV')

# Data is arranged alphabetically from A-Z      
df = df.sort_values(by='Name').reset_index(drop=True)

# S.No index is start from 1
df.index = np.arange(1, len(df) + 1)
df.index.name = 'S.No'
print(f"Total students loaded: {len(df)}")

# Calculations
subjects = ['Engg_Physics', 'Engg_Chemistry', 'Mathematics', 'English', 'Engg_Computer']
df['Grand_Total(750)'] = np.sum(df[subjects], axis=1)
df['Percentage(%)'] = np.round((df['Grand_Total(750)'] / 750) * 100, 2)

# Pass Logic: Percentage >= 40 aur Attendance >= 70
df['Status'] = np.where((df['Percentage(%)'] >= 40) & (df['Attendance_Per'] >= 70), 'Pass', 'Fail')
df['Grade'] = [assign_grade(p) for p in df['Percentage(%)']]

# Terminal display settings for wide table
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("\n--- 2. Detailed Student Performance Report ---")
columns_to_print = ['Name', 'Department'] + subjects + ['Attendance_Per', 'Grand_Total(750)', 'Percentage(%)', 'Status', 'Grade']
print(df[columns_to_print].to_string())

print("\n--- 3. Overall Class Performance Analysis ---")
class_avg = np.round(np.mean(df['Percentage(%)']), 2)
lowest_mark = np.min(df['Percentage(%)'])
passed_students = len(df[df['Status'] == 'Pass'])
failed_students = len(df) - passed_students

print(f"-> Overall Class Percentage: {class_avg}%")
print(f"-> Lowest Percentage in Class: {lowest_mark}%")
print(f"-> Total Students Passed: {passed_students} out of {len(df)} (Failed: {failed_students})")

print("\n--- 4. Top 3 Performers ---")
top_3 = df.nlargest(3, 'Percentage(%)')
rank = 1
for _, row in top_3.iterrows():
    print(f"Rank {rank}: {row['Name']} ({row['Department']}) - {row['Grand_Total(750)']}/750 ({row['Percentage(%)']}%) - Grade {row['Grade']}")
    rank += 1

print("\n--- 5. Subject-wise Analysis (Out of 150) ---")
for sub in subjects:
    sub_avg = np.round(np.mean(df[sub]), 2)
    sub_pass = len(df[df[sub] >= 50]) # Passing criteria 50/150
    sub_pass_percent = np.round((sub_pass / len(df)) * 100, 2)
    
    # Highest aur Lowest score nikalna unke naam ke saath
    sub_max = df[sub].max()
    sub_min = df[sub].min()
    max_student = df[df[sub] == sub_max]['Name'].iloc[0]
    min_student = df[df[sub] == sub_min]['Name'].iloc[0]
    
    print(f"\n-> {sub}:")
    print(f"   Average Score: {sub_avg}/150 | Pass Percentage: {sub_pass_percent}% ({sub_pass} Passed)")
    print(f"   Highest: {sub_max} ({max_student}) | Lowest: {sub_min} ({min_student})")

print("\n--- 6. Department-wise Average Performance ---")
dept_avg = df.groupby('Department')['Percentage(%)'].mean().round(2)
for dept, avg in dept_avg.items():
    print(f"-> {dept} Department Average: {avg}%")

print("\n" + "="*75)
print("                       END OF ANALYSIS REPORT")
print("="*75 + "\n")


