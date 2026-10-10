# 1. Project Title
**EWB Student Performance Analytics System**
- **Student Name:** Kushal Mani Tripathi
- **Role:** Python with AI Intern
- **Institution:** EWB Edutech

# 2. Objective
The objective of this project is to build an automated data analytics system that processes raw student academic records. It solves the problem of manual grade calculation and performance tracking by evaluating total marks, percentages, pass/fail status based on attendance, and providing subject-wise and department-wise insights.

# 3. Technologies Used
- **Python 3:** Core programming language.
- **NumPy:** Used for fast mathematical calculations (sums, averages) and logical conditions (`np.where`).
- **Pandas:** Used for data manipulation, loading CSV files, grouping data by department, and generating structured terminal reports.

# 4. Dataset Description
The dataset (`STUDENT.CSV`) contains 20 student records with the following key columns:
- `Student_ID`, `Name`, `Department` (ECE, CSE, Civil, Mechanical)
- Marks for 5 engineering subjects (Engg_Physics, Engg_Chemistry, Mathematics, English, Engg_Computer) out of 150 each.
- `Attendance_Per` (Attendance percentage).

# 5. Implementation
1. **Data Loading:** Loaded the CSV file using `pd.read_csv()` and sorted students alphabetically using `sort_values()`.
2. **Calculations:** Used `np.sum()` across subject columns to calculate `Grand_Total(750)` and basic arithmetic for `Percentage(%)`.
3. **Conditions:** Applied `np.where()` to check if a student scored >= 40% AND had >= 70% attendance to determine the 'Pass' or 'Fail' `Status`.
4. **Functions:** Implemented a custom `assign_grade(percentage)` function inside a list comprehension to assign A, B, C, or F grades.
5. **Analytics:** Utilized `np.mean()`, `max()`, `min()`, and Pandas `groupby()` to extract class averages, subject-wise pass ratios, and department-wise performance.

# 6. Key Features
- Alphabetical data sorting and clean tabular display.
- Automated total and percentage calculations.
- Pass/Fail logic incorporating both academic and attendance criteria.
- Top 3 Performers ranking.
- Subject-wise insights (Highest/Lowest scorers with names, Pass/Fail ratios).
- Department-wise average percentage calculation.

# 7. Output / Screenshots
<img width="1920" height="1080" alt="Screenshot (127)" src="https://github.com/user-attachments/assets/10303bd8-6b78-49f9-b78a-8b5ccec0d988" />
<img width="1920" height="1080" alt="Screenshot (128)" src="https://github.com/user-attachments/assets/2f2cc386-5f6e-4112-aef2-1bd5ec29bcde" />

# 8. Final Outcome
The project successfully automated the processing of 20 student records. It generated a clean, readable terminal report showing individual performance, identified the Top 3 students across the college, and provided a clear breakdown of how each department and subject performed overall.

# 9. Challenges & Learning
- **Challenge:** The Pandas dataframe was wrapping text to the next line in the terminal, breaking the table format.
- **Solution:** Configured Pandas display options (`pd.set_option('display.expand_frame_repr', False)`) to prevent line wrapping and show all columns cleanly.
- **Learning:** Gained hands-on experience using NumPy for vectorized operations over standard loops, and learned how to use Pandas `groupby` to aggregate data effectively.

# 10. GitHub Repository
https://github.com/kushal6261/STUDENT-PERFORMANCE-ANALYTICS
