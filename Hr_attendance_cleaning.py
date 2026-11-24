import pandas as pd 

udaiveersingh = pd.read_csv("02_hr_attendance.csv")
print(udaiveersingh.shape)
print(udaiveersingh.columns)
print(udaiveersingh.size)
print(udaiveersingh.info())
print(udaiveersingh.describe())
print(udaiveersingh.head())

print(udaiveersingh.isna().sum())
print(udaiveersingh.duplicated().sum())

udaiveersingh = udaiveersingh.drop_duplicates()

udaiveersingh["date"] = pd.to_datetime(udaiveersingh["date"], errors="coerce")

udaiveersingh["department"] = (
    udaiveersingh["department"].fillna("Unknown")
    .astype("string").str.strip().str.title()
)
udaiveersingh["work_mode"] = (
    udaiveersingh["work_mode"].fillna("Unknown")
    .astype("string").str.strip().str.title()
)
udaiveersingh["performance_rating"] = pd.to_numeric(udaiveersingh["performance_rating"],errors="coerce")
udaiveersingh["performance_rating"] = (udaiveersingh["performance_rating"].fillna(0))

udaiveersingh["Is_absent"] = udaiveersingh["attendance_status"].eq("Absent")
udaiveersingh["Is_late"] = udaiveersingh["late_arrival"].eq("Yes")
udaiveersingh["Full_day_work"] = udaiveersingh["hours_worked"] >= 7.5
udaiveersingh["Month"] = udaiveersingh["date"].dt.to_period("M").astype("string")

attendance_status = udaiveersingh["attendance_status"].value_counts(dropna=False)
department_count = udaiveersingh["department"].value_counts(dropna=False)
print(attendance_status)
print(department_count)


udaiveersingh.to_csv("Hr_attendance_cleaned.csv")



"Close The Project"
