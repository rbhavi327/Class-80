
import pandas as pd
 
print("================================")
print("STUDENT MARKS ANALYSER")
print("================================")

marks = [88, 76, 92, 67, 85]
 
student_marks = pd.Series(
    marks,
    index=["Aarav", "Meera", "Kabir", "Anaya", "Rohan"]
)
 
print(student_marks)

data = {
    "Student": ["Aarav", "Meera", "Kabir", "Anaya", "Rohan"],
    "Math": [88, 76, 92, 67, 85],
    "Science": [91, 80, 89, 72, 87],
    "English": [84, 78, 95, 70, 82],
    "Attendance": [96, 90, 98, 85, 92]
}
 
df = pd.DataFrame(data)
 
print(df)
 
df.to_csv("student_marks.csv", index=False)
 
student_data = pd.read_csv("student_marks.csv")
 
print("CSV file read successfully!")
print(student_data)
 

print("First 3 rows:")
print(student_data.head(3))
 
print("Last 2 rows:")
print(student_data.tail(2))
 
print("Data Information:")
print(student_data.info())
 